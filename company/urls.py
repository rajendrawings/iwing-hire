from django.urls import path, include

from .views import (
    CompanyListApiView,
    SubscriptionListApiView,
    SubscriptionDetailApiView,
    CompanySubscriptionListAPIView
)

urlpatterns = [
    path('company/companys', CompanyListApiView.as_view()),
    path('company/subscriptions', SubscriptionListApiView.as_view()),
    path('company/subscription/<int:pk>', SubscriptionDetailApiView.as_view()),
    path('company/companysubscription', CompanySubscriptionListAPIView.as_view()),
]