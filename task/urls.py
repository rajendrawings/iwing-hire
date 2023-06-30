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

#Below urls for ActivityFiles
    path('activityfile', ActivityFileApiView.as_view()),
    path('activityfile/<int:pk>', ActivityFileDetailApiView.as_view()),



    #Below urls for Board.................
    # path('board',ApiOverView, name='home'),
    # path('add', add_boards, name='add_board'),
    # path('list', view_board, name='list'),
    # path('board/<int:pk>', get_boards, name='get_boards'),
    # path('update/<int:pk>', update_board, name='update_board'),
    # path('boards/<int:pk>', delete_board, name='delete-board'),

    # #Below urls is for Card...............
    # path('card',ApiOverViewCard, name='cardhome'),
    # path('create_cards',add_cards, name='create_cards'),
    # path('list_cards', view_cards, name='list_cards'),

]