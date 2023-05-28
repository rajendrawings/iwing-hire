from django.urls import path, include
from .views import (
    ProfileApiView,
    ProfileDetailApiView,
    RoleListApiView
)

urlpatterns = [
    path('profile', ProfileApiView.as_view()),
    path('profile-details', ProfileDetailApiView.as_view()),
    path('role', RoleListApiView.as_view()),
]