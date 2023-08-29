from django.urls import path, include
from .views import *


urlpatterns = [
    #Below urls for Board
    path('board', BoardApiView.as_view()),
    path('board/<int:pk>', BoardDetailApiView.as_view()),

    #Below urls for card
    path('card', CardApiView.as_view()),
    path('card/<int:pk>', CardDetailApiView.as_view()),

    #Below urls for Task
    path('task', TaskApiView.as_view()),
    path('task/<int:pk>', TaskDetailApiView.as_view()),

    #Below urls for Activity
    path('activity', ActivityApiView.as_view()),
    path('activity/<int:pk>', ActivityDetailApiView.as_view()),

    #Below urls for Jobs
    path('job', JobApiView.as_view()),
    path('job/<int:pk>', JobDetailApiView.as_view()),

    #Below urls for Interviewer
    path('interviewer', InterviewerApiView.as_view()),
    path('interviewer/<int:pk>', InterviewerDetailApiView.as_view()),
    path('import_interviewer',InterviewerImportAPI.as_view())



    





   
]