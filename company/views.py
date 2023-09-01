from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .models import Company, Subscription, CompanySubscription
from .serializers import CompanySerializer, SubscriptionSerializer, CompanySubscriptionSerializer
from drf_yasg.utils import swagger_auto_schema

class CompanyListApiView(APIView):
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=['Company'],
    )
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the company items for given requested user
        '''
        companys = Company.objects.all()
        serializer = CompanySerializer(companys, many=True)
        response_data = {
            "status" : "success",
            "message" : "List of company retrieved successfully",
            "data" : serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['Company'],
    )
    # 2. Create
    def post(self,request, *args, **kwargs):
        '''
        Create the Company with given company data
        '''
        subscription_id = request.data.get("subscription_id", None)
        serializer = CompanySerializer(data=request.data, context = {"user": request.user, "subscription_id": subscription_id})
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "status" : "success",
                "message" : "company saved successfully",
                "data" : serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionListApiView(APIView):
    
    serializer_class = SubscriptionSerializer
 
    @swagger_auto_schema(
        tags=['Subscription'],
    )
    def get(self, request, *args, **kwargs):
        '''
        Get Subscriptions List
        '''
        queryset = Subscription.objects.all()
        serializer = SubscriptionSerializer(queryset, many=True)
        response_data = {
            "status" : "success",
            "message": "subscription retrieved successfully",
            "data": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['Subscription'],
    )
    def post(self, request, *args, **kwargs):
        '''
        post subscription data
        '''
        data = {}
        subscriptions = SubscriptionSerializer(data=request.data)
        if subscriptions.is_valid():
            subscriptions.save()
            response_data = {
                "status": "success",
                "message" : "subscription saved succesfully",
                "data" : subscriptions.data

            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SubscriptionDetailApiView(APIView):
    serializer_class = SubscriptionSerializer

    @swagger_auto_schema(
        tags=['Subscription'],
    )
    def get(self, request, pk=None):
        '''
        get single subscription
        '''
        if pk:
            try:
                subscription = Subscription.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if subscription:
                serializer = SubscriptionSerializer(subscription)
                response_data = {
                    "status" : "success",
                    "message" : "subscription retrieved successfully",
                    "data" : serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(
        tags=['Subscription'],
    )
    def put(self, request, pk=None):
        '''
        update subscription
        '''
        subscription = Subscription.objects.get(pk=pk)
        data = SubscriptionSerializer(instance=subscription, data=request.data)
        if data.is_valid():
            data.save()
            response_data = {
                "status": "success",
                "message" : "subscription updated successfully",
                "data" : data.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=['Subscription'],
    )
    def delete(self, request,pk=None):
        '''
        delete subscription
        '''
        subscription = get_object_or_404(Subscription,pk=pk)
        subscription.delete()
        response_data = {
            "status" : "success",
            "message" : "subscription deleted successfully",
        }
        return Response(response_data,status=status.HTTP_204_NO_CONTENT)


class CompanySubscriptionListAPIView(APIView):
    serializer_class = CompanySubscriptionSerializer

    @swagger_auto_schema(
        tags=['CompanySubscription'],
    )
    def get (self, request, *args, **kwargs):
        '''
        List all the company subscription 
        '''
        companysubscriptions = CompanySubscription.objects.all()
        serializer = CompanySubscriptionSerializer(companysubscriptions, many=True)
        response_data = {
            "status" : "success",
            "message" : "companysubscription retrieved successfully",
            "data" : serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['CompanySubscription'],
    )
    def post(self, request, *args, **kwargs):
        '''
        post companysubscription data
        '''
        data = {}
        companysubscriptions = CompanySubscriptionSerializer(data=request.data)
        if companysubscriptions.is_valid():
            companysubscriptions.save()
            response_data = {
                "status": "success",
                "message": "Subscription activate successfully.",
                "data": companysubscriptions.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(companysubscriptions.errors, status=status.HTTP_400_BAD_REQUEST)