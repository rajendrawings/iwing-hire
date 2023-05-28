from django.urls import path, include
from .views import (
    CompanyListApiView,
)

urlpatterns = [
    path('companys', CompanyListApiView.as_view()),
]