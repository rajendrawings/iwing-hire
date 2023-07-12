from django.urls import path, include
#from rest_framework.authtoken import views as authtoken_views

from .views import (
    CompanyListApiView,
)

urlpatterns = [
    path('companys', CompanyListApiView.as_view()),
]