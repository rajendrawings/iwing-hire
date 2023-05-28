from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from .models import Profile, Role
from .serializers import GetProfileSerializer, ProfileSerializer, RoleSerializer


class ProfileDetailApiView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    # 1. Get Details
    def get(self, request, *args, **kwargs):
        '''
        Get user profile details
        '''
        user_obj = Profile.objects.filter(user=request.user)
        if user_obj:
            serializer = GetProfileSerializer(user_obj[0],)
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
            'role': request.data.get('role')
        }
        if data['password'] != data['confirm_password']:
            return Response({"Error": "Password fields didn't match"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_obj = Profile.objects.filter(Q(user__username=data["email"]) | Q(user__email=data["email"]))
        if user_obj:
            return Response({"Error": "Email already exits"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            profile_obj = Profile.objects.filter(Q(user__username=data["email"]) | Q(user__email=data["email"])).first()
            profile_serializer = GetProfileSerializer(profile_obj,)
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RoleListApiView(APIView):
    serializer_class = RoleSerializer

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        Get all role
        '''
        user_obj = Role.objects.all()
        serializer = RoleSerializer(user_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RoleApiView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RoleSerializer

    def post(self, request, *args, **kwargs):
        '''
        Create Role
        '''
        role = request.data.get('role')
        if role:
            data = {"role": role}
            serializer = RoleSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Error": "role name required"}, status=status.HTTP_400_BAD_REQUEST)