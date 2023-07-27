from django.urls import path, include
#from rest_framework.authtoken import views as authtoken_views

from .views import (
    CompanyListApiView,
    SubscriptionListApiView,
    SubscriptionDetailApiView
)

urlpatterns = [
    path('companys', CompanyListApiView.as_view()),
    path('subscriptions', SubscriptionListApiView.as_view()),
    path('subscription/<int:pk>', SubscriptionDetailApiView.as_view()),

]