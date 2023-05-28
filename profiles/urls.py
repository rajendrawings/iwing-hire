from django.urls import path, include
from .views import (
    ProfileApiView,
    ProfileDetailApiView,
    RoleListApiView,
    RoleApiView
)

urlpatterns = [
    path('profile', ProfileApiView.as_view()),
    path('profile-details', ProfileDetailApiView.as_view()),
    path('role', RoleListApiView.as_view()),
    path('create-role', RoleApiView.as_view()),
]