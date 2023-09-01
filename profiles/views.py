from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Profile, Hr, Candidate, CompanysCandidates, HRGroup
from .serializers import( 
    GetProfileSerializer, 
    ProfileSerializer, 
    HrSerializer, 
    GetHrSerializer, 
    CandidateSerializer, 
    GetCandidateSerializer, 
    HRGroupSerializer, 
    HrSerializer,
)
from company.models import Company
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema



class ProfileDetailApiView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=['Profile'],
    )
    # 1. Get Details
    def get(self, request, *args, **kwargs):
        '''
        Get user profile details
        '''
        user_obj = Profile.objects.filter(user=request.user)
        hr_obj = Hr.objects.filter(user=request.user)
        if user_obj:
            serializer = GetProfileSerializer(user_obj[0], many=False)
            response_data = {
                "status" : "success",
                "message" : "user objects retrieved successfully",
                "data" : serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        elif hr_obj:
            serializer = GetHrSerializer(hr_obj[0], many=False)
            response_data = {
                "status" : "success",
                "message" : "Hr objects retrieved successfully",
                "data" :serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        
        return Response({"Error": "User profile does not exits"})
    

class ProfileApiView(APIView):
    serializer_class = ProfileSerializer

    @swagger_auto_schema(
        tags=['Profile'],
    )
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
            response_data = {
                "status" : "success",
                "message" : "profile saved successfully",
                "data" : profile_serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateApiView(APIView):
    serializer_class = CandidateSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=['Candidate'],
    )
    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the candidate user with given candidate data
        '''
        data = {
            'email': request.data.get('email'), 
            'password': request.data.get('password'), 
            'confirm_password': request.data.get('confirm_password'),
            'role': request.data.get('role'),
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
            response_data = {
                "status" : "success",
                "message" : "candidate saved successfully",
                "data" : candidate_serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HRGroupListApiView(APIView):
    serializer_class = HRGroupSerializer

    @swagger_auto_schema(
        tags=['HRGroup'],
    )
    def get(self, request, *args, **kwargs):
        '''
        get Hr Group list
        '''                                                                                                                                                                                                                                                                       
        hr_groups = HRGroup.objects.all()
        serializer = HRGroupSerializer(hr_groups, many=True)
        response_data = {
            "status" : "success",
            "message" : "List of  HRGroup",
            "data" : serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['HRGroup'],
    )
    def post(self, request, *args, **Kwargs):
        '''
        create HRGroup 
        '''
        hr_group = HRGroupSerializer(data = request.data)
        if hr_group.is_valid():
            hr_group.save()
            response_data = {
                "status" : "success",
                "message" : "HRGroup created successfully",
                "data" : hr_group.data
            }
            return Response(response_data)
        else:
            message= "Please enter valid data"
            return Response(message, status.HTTP_404_NOT_FOUND)


class HRGroupDetailApiView(APIView):
    serializer_class= HRGroupSerializer

    @swagger_auto_schema(
        tags=['HRGroup'],
    )
    def get(self, request, pk=None):
        '''
        get single Hr-Group
        '''
        if pk:
            try:
                hr_group = HRGroup.objects.get(pk=pk)
            except:
                message= "Data not found"
                return Response(message, status=status.HTTP_404_NOT_FOUND)

            if hr_group:
                serializer = HRGroupSerializer(hr_group)
                response_data = {
                    "status" : "success",
                    "message" : "HRGroup retrieved successfully",
                    "data" : serializer.data
                }
                return Response(response_data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            message= "Invalid data"
            return Response (message, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=['HRGroup'],
    )
    def put(self, request, pk=None):
        '''
        Update data
        '''
        # hr_group = HRGroup.objects.get(pk=pk)
        try:
            hr_group = HRGroup.objects.get(pk=pk)
        except HRGroup.DoesNotExist:
            return Response({"error": "HRGroup not found"}, status=status.HTTP_404_NOT_FOUND)

        data = HRGroupSerializer(instance= hr_group, data= request.data)
        if data.is_valid():
            data.save()
            response_data = {
                "status" : "success",
                "message" : "HRgroup updated successfully",
                "data" : data.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            message= "data not found"
            return Response(message,status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=['HRGroup'],
    )
    def delete(self, request,pk=None):
        '''
        delete Hr-Group
        '''
        hr_group = get_object_or_404(HRGroup, pk=pk)
        hr_group.delete()
        response_data = {
            "status" : "success",
            "message" : "HRGroup deleted successfully",
        }
        return Response(response_data, status=status.HTTP_202_ACCEPTED)


class HrListApiView(APIView):
    serializer_class = HrSerializer

    @swagger_auto_schema(
        tags=['Hr'],
    )
    def get(self, request, *args, **kwargs):
        '''
        get Hr list
        '''
        hr = Hr.objects.all()
        serializer = HrSerializer(hr, many=True)
        response_data= {
            "status" : "success",
            "message" : "List of Hr ",
            "data" : serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['Hr'],
    )
    def post(self, request, *args, **kwargs):
        '''
        Create Hr
        '''
        # filter and check email already exits or not
        email = request.data.get('email')

        existing_user = User.objects.filter(email=email).exists()
        if existing_user:
            return Response({'detail': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = HrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "status" : "success",
                "message" : "Hr Created Successfully",
                "data" : serializer.data
            }
            return Response(response_data)
        else:
            response_data = {
                "status" : "Failed",
                "message" : "Please enter valid data"
            }
            message = serializer.errors
            return Response(response_data, status= status.HTTP_404_NOT_FOUND)


class HrDetailApiView(APIView):
    serializer_class = HrSerializer

    @swagger_auto_schema(
        tags=['Hr'],
    )
    def get(self, request, pk=None):
        '''
        get single Hr detail
        '''
        if pk:
            try:
                hr = Hr.objects.get(pk=pk)
            except:
                message = "Data Not Found"
                return Response(message, status=status.HTTP_404_NOT_FOUND)

            if hr:
                serializer = HrSerializer(hr)
                response_data = {
                    "status" : "success",
                    "message" : "Hr retrived Successfully",
                    "data" : serializer.data
                }
                return Response(response_data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            response_data = {
                "status" : "Failed",
                "message" : "Invalid Data",
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=['Hr'],
    )
    def put(self, request, pk=None):
        '''
        update Hr
        '''
        try:
            hr = Hr.objects.get(pk=pk)
        except:
            return Response({"error" : "Hr not found"}, status=status.HTTP_404_NOT_FOUND)

        data = HrSerializer(instance= hr, data= request.data)
        if data.is_valid():
            data.save()
            response_data ={
                "status": "success",
                "message" : "Hr Updated successfully",
                "data" : data.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                "status" : "Failed",
                "message" : "Data not Found",
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)   

    @swagger_auto_schema(
        tags=['Hr'],
    )
    def delete(sef, request, pk=None):
        '''
        delete Hr
        '''
        hr = get_object_or_404(Hr, pk=pk)
        hr.delete()
        response_data = {
            "status" : "success",
            "message" : "Hr deleted successfully",
        }
        return Response(response_data, status=status.HTTP_202_ACCEPTED)


