from django.urls import path, include
from .views import (
    ProfileApiView,
    ProfileDetailApiView,
    CandidateApiView
)

urlpatterns = [
    path('profile', ProfileApiView.as_view()),
    path('profile-details', ProfileDetailApiView.as_view()),
    path('add-candidate', CandidateApiView.as_view())
]