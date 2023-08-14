from django.urls import path, include
from .views import (
    ProfileApiView,
    ProfileDetailApiView,
    CandidateApiView,
    HRGroupListApiView,
    HRGroupDetailApiView
)

urlpatterns = [
    path('profile', ProfileApiView.as_view()),
    path('profile-details', ProfileDetailApiView.as_view()),
    path('add-candidate', CandidateApiView.as_view()),

    # For Hr_Group
    path('hr-group/', HRGroupListApiView.as_view()),
    path('hr-group/<int:pk>',HRGroupDetailApiView.as_view()),
]