from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .models import Company, Subscription
from .serializers import CompanySerializer, SubscriptionSerializer

class CompanyListApiView(APIView):
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)

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
        # data = {
        #     'task': request.data.get('task'), 
        #     'completed': request.data.get('completed'), 
        #     'user': request.user.id
        # }
        data = {
            'name' : request.data.get('name'),
            'user' : request.user.id
        }
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionListApiView(APIView):
    serializer_class = SubscriptionSerializer

    def get(self, request, *args, **kwargs):
        '''
        Get Subscriptions List
        '''
        queryset = Subscription.objects.all()
        serializer = SubscriptionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        '''
        post subscription data
        '''
        data = {}
        subscriptions = SubscriptionSerializer(data=request.data)
        if subscriptions.is_valid():
            subscriptions.save()
            return Response(subscriptions.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SubscriptionDetailApiView(APIView):
    serializer_class = SubscriptionSerializer

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
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        '''
        update subscription
        '''
        subscription = Subscription.objects.get(pk=pk)
        data = SubscriptionSerializer(instance=subscription, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request,pk=None):
        '''
        delete subscription
        '''
        subscription = get_object_or_404(Subscription,pk=pk)
        Subscription.delete()
        return Response(status=status.HTTP_202_ACCEPTED)