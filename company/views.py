from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from .models import Company
from .serializers import CompanySerializer

class CompanyListApiView(APIView):
    permission_classes = [TokenAuthentication]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the company items for given requested user
        '''
        companys = Company.objects.all()
        serializer = CompanySerializer(companys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Company with given company data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)