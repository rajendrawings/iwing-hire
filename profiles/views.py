from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Profile, Hr, Candidate, CompanysCandidates
from .serializers import GetProfileSerializer, ProfileSerializer, HrSerializer, GetHrSerializer, CandidateSerializer, GetCandidateSerializer
from company.models import Company
from django.db.models import Q
from django.contrib.auth.models import User

class ProfileDetailApiView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    # 1. Get Details
    def get(self, request, *args, **kwargs):
        '''
        Get user profile details
        '''
        user_obj = Profile.objects.filter(user=request.user)
        hr_obj = Hr.objects.filter(user=request.user)
        if user_obj:
            serializer = GetProfileSerializer(user_obj[0], many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif hr_obj:
            serializer = GetHrSerializer(hr_obj[0], many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"Error": "User profile does not exits"})
    

class ProfileApiView(APIView):
    serializer_class = ProfileSerializer

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the user profile with given user data
        '''
        data = {
            'email': request.data.get('email'), 
            'password': request.data.get('password'), 
            'confirm_password': request.data.get('confirm_password'),
        }
        if data['password'] != data['confirm_password']:
            return Response({"Error": "Password fields didn't match"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_obj = User.objects.filter(Q(username=data["email"]) | Q(email=data["email"]))
        if user_obj:
            return Response({"Error": "Email already exits"}, status=status.HTTP_400_BAD_REQUEST)
    
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            profile_obj = Profile.objects.filter(Q(user__username=data["email"]) | Q(user__email=data["email"])).first()
            profile_serializer = GetProfileSerializer(profile_obj,)
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateApiView(APIView):
    serializer_class = CandidateSerializer
    permission_classes = (IsAuthenticated,)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the candidate user with given candidate data
        '''
        data = {
            'email': request.data.get('email'), 
            'password': request.data.get('password'), 
            'confirm_password': request.data.get('confirm_password'),
            'role': request.data.get('role').lower(),
            'company': request.data.get('company'),
        }
        if data['password'] != data['confirm_password']:
            return Response({"Error": "Password fields didn't match"}, status=status.HTTP_400_BAD_REQUEST)
        
        company_obj = Company.objects.filter(id=data['company'])
        if not company_obj:
            return Response({"Error": "Company does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_obj = User.objects.filter(Q(username=data["email"]) | Q(email=data["email"]))
        if user_obj:
            candidate_data = {
                "user_id": user_obj[0].id
            }
            candidate = Candidate.objects.filter(user_id=user_obj[0].id).first()
            company_candidate_obj = CompanysCandidates.objects.filter(company_id=company_obj[0].id).first()
            if not company_candidate_obj:
                company_candidate_obj = CompanysCandidates.objects.create(company_id=company_obj[0].id)
            company_candidate_obj.candidate.add(candidate)
            candidate_serializer = GetCandidateSerializer(candidate)
            return Response(candidate_serializer.data, status=status.HTTP_201_CREATED)
        
        serializer = CandidateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            candidate_obj = Candidate.objects.filter(Q(user__username=data["email"]) | Q(user__email=data["email"])).first()
            candidate_serializer = GetCandidateSerializer(candidate_obj,)
            return Response(candidate_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
