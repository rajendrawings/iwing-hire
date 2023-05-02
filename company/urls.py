from django.urls import path, include
from .views import (
    CompanyListApiView,
)

urlpatterns = [
    path('', CompanyListApiView.as_view()),
]