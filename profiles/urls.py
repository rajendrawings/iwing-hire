from django.urls import path, include
from .views import (
    ProfileApiView,
    ProfileDetailApiView,
    CandidateApiView,
    HRGroupListApiView,
    HRGroupDetailApiView,
    HrListApiView,
    HrDetailApiView,
)

urlpatterns = [
    path('profile/profile', ProfileApiView.as_view()),
    path('profile/profile-details', ProfileDetailApiView.as_view()),
    path('profile/add-candidate', CandidateApiView.as_view()),

    # For Hr_Group
    path('profile/hr-group/', HRGroupListApiView.as_view()),
    path('profile/hr-group/<int:pk>',HRGroupDetailApiView.as_view()),

    # for Hr
    path('profile/hr', HrListApiView.as_view()),
    path('profile/hr/<int:pk>', HrDetailApiView.as_view()),

]