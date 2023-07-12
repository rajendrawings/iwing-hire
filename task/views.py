from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .models import Board
from .serializers import BoardSerializer, CardSerializer, TaskSerializer, GetTaskSerializer, ActivitySerializer, JobSerializer
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Card
from.models import Task
from.models import Activity
from.models import Job

#Board views
class BoardApiView(APIView):
    serializer_class = BoardSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        '''
        Get Board List
        '''
        queryset = Board.objects.all()
        if request.query_params:
            boards = Board.objects.filter(**request.query_params.dict())
        else:
            boards = Board.objects.all()

        if boards:
            serializer = BoardSerializer(boards, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        '''
         Post data
         '''
        boards = BoardSerializer(data=request.data)
        if boards.is_valid():
            boards.save()
            return Response(boards.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
class BoardDetailApiView(APIView):
    serializer_class = BoardSerializer
    
    def get(self, request, pk=None):
        '''
        get single board
        '''
        if pk:
            try:
                board = Board.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if board:
                serializer = BoardSerializer(board)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        '''
        update Board
        '''
        board = Board.objects.get(pk=pk)
        data = BoardSerializer(instance=board, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete board
        '''
        board = get_object_or_404(Board, pk=pk)
        board.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    
#card views
class CardApiView(APIView):
    serializer_class = CardSerializer
    
    def get(self, request, *args, **kwargs):
        '''
        Get card List
        '''
        queryset = Card.objects.all()
        if request.query_params:
            cards = Card.objects.filter(**request.query_params.dict())
        else:
            cards = Card.objects.all()

        if cards:
            serializer = CardSerializer(cards, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        '''
         Post data
         '''
        cards = CardSerializer(data=request.data)
        if cards.is_valid():
            cards.save()
            return Response(cards.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CardDetailApiView(APIView):
    serializer_class = CardSerializer

    def get(self, request, pk=None):
        '''
        get single card
        '''
        if pk:
            try:
                card = Card.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if card:
                serializer = CardSerializer(card)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        '''
        update card
        '''
        card = Card.objects.get(pk=pk)
        data = CardSerializer(instance=card, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete card
        '''
        card = get_object_or_404(Card, pk=pk)
        card.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


#Task views
class TaskApiView(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request, *args, **kwargs):
        '''
        Get Task List
        '''
        queryset = Task.objects.all()
        if request.query_params:
            tasks = Task.objects.filter(**request.query_params.dict())
        else:
            tasks = Task.objects.all()

        if tasks:
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        '''
         Post Task data
         '''
        tasks = TaskSerializer(data=request.data)
        if tasks.is_valid():
            tasks.save()
            return Response(tasks.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
class TaskDetailApiView(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request, pk=None):
        '''
        get single Task
        '''
        if pk:
            try:
                task = Task.objects.get(pk=pk)
            except:
                print("Error")
                return Response(status=status.HTTP_404_NOT_FOUND)

            if task:
                serializer = GetTaskSerializer(task)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        '''
        update Task
        '''
        task = Task.objects.get(pk=pk)
        data = TaskSerializer(instance=task, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete Task
        '''
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


#Activity views
class ActivityApiView(APIView):
    serializer_class = ActivitySerializer
    
    def get(self, request, *args, **kwargs):
        '''
        Get Activity List
        '''
        queryset = Activity.objects.all()
        if request.query_params:
            activitys = Activity.objects.filter(**request.query_params.dict())
        else:
            activitys = Activity.objects.all()

        if activitys:
            serializer = ActivitySerializer(activitys, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        '''
         Post  Activity data
         '''
        data = {}
        # data["file"] = request.dt
        # data["task"] = request.data.task
        # data["comment"] = request.data.comment

        activitys = ActivitySerializer(data=request.data)
        if activitys.is_valid():
            activitys.save()
            return Response(activitys.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
class ActivityDetailApiView(APIView):
    serializer_class = ActivitySerializer
    
    def get(self, request, pk=None):
        '''
        get single Activity
        '''
        if pk:
            try:
                activity = Activity.objects.get(pk=pk)
            except:
                print("Error")
                return Response(status=status.HTTP_404_NOT_FOUND)

            if activity:
                serializer = ActivitySerializer(activity)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        '''
        update Activity
        '''
        activity = Activity.objects.get(pk=pk)
        data = ActivitySerializer(instance=activity, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete Activity
        '''
        activity = get_object_or_404(Activity, pk=pk)
        activity.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


#Job views
class JobApiView(APIView):
    serializer_class = JobSerializer

    def get(self, request, *args, **kwargs):
        '''
        Get Job List
        '''
        queryset = Job.objects.all()
        if request.query_params:
            jobs = Job.objects.filter(**request.query_params.dict())
        else:
            jobs = Job.objects.all()

        if jobs:
            serializer = JobSerializer(jobs, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        '''
         Post  Job data
         '''
        data = {}
        # data["file"] = request.dt
        # data["task"] = request.data.task
        # data["comment"] = request.data.comment

        jobs = JobSerializer(data=request.data)
        if jobs.is_valid():
            jobs.save()
            return Response(jobs.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class JobDetailApiView(APIView):
    serializer_class = JobSerializer

    def get(self, request, pk=None):
        '''
        get single Job
        '''
        if pk:
            try:
                job = Job.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if job:
                serializer = JobSerializer(job)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        '''
        update Job
        '''
        job = Job.objects.get(pk=pk)
        data = JobSerializer(instance=job, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete job
        '''
        job = get_object_or_404(Job, pk=pk)
        job.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


    







 

    


    


    







    




  



    

    
    


    


        
        





