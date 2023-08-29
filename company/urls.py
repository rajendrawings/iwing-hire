from django.urls import path, include

from .views import (
    CompanyListApiView,
    SubscriptionListApiView,
    SubscriptionDetailApiView,
    CompanySubscriptionListAPIView
)

urlpatterns = [
    path('companys', CompanyListApiView.as_view()),
    path('subscriptions', SubscriptionListApiView.as_view()),
    path('subscription/<int:pk>', SubscriptionDetailApiView.as_view()),
    path('companysubscription', CompanySubscriptionListAPIView.as_view()),
]