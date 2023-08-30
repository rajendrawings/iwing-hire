from django.urls import path, include
from .views import *

urlpatterns = [
    # Below urls for Board
    path('task/board', BoardApiView.as_view()),
    path('task/board/<int:pk>', BoardDetailApiView.as_view()),

    # Below urls for card
    path('task/card', CardApiView.as_view()),
    path('task/card/<int:pk>', CardDetailApiView.as_view()),

    # Below urls for Task
    path('task/task', TaskApiView.as_view()),
    path('task/task/<int:pk>', TaskDetailApiView.as_view()),

    # Below urls for Activity
    path('task/activity', ActivityApiView.as_view()),
    path('task/activity/<int:pk>', ActivityDetailApiView.as_view()),

    # Below urls for Jobs
    path('task/job', JobApiView.as_view()),
    path('task/job/<int:pk>', JobDetailApiView.as_view()),

    # Below urls for Interviewer
    path('task/interviewer', InterviewerApiView.as_view()),
    path('task/interviewer/<int:pk>', InterviewerDetailApiView.as_view()),
    path('task/import_interviewer', InterviewerImportAPI.as_view())

]
