from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
import odf
from .models import Board
from .serializers import (
    BoardSerializer, 
    CardSerializer, 
    TaskSerializer, 
    GetTaskSerializer, 
    ActivitySerializer, 
    JobSerializer, 
    InterviewerSerializer, 
    InterviewerSerializer1
)
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Card
from.models import Task
from.models import Activity
from.models import Job
from.models import Interviewer
import pandas as pd
import uuid
from drf_yasg.utils import swagger_auto_schema


#Board views
class BoardApiView(APIView):
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=['Board'],
    )
    def get(self, request, *args, **kwargs):
        '''
        Get Board List
        '''
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        response_data = {
            "status" : "success",
            "message" : "List of board retrieved successfully",
            "data" : serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['Board'],
    )
    def post(self, request, *args, **kwargs):
        '''
         Post data
         '''
        boards = BoardSerializer(data=request.data)
        if boards.is_valid():
            boards.save()
            response_data = {
                "status" : "success",
                "message" : "Board saved successfully",
                "data" : boards.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class BoardDetailApiView(APIView):
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=['Board'],
    )
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
                response_data = {
                    "status" : "success",
                    "message" : "Board retrieved successfully",
                    "data" : serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=['Board'],
    )
    def put(self, request, pk=None):
        '''
        update Board
        '''
        board = Board.objects.get(pk=pk)
        data = BoardSerializer(instance=board, data=request.data)
        if data.is_valid():
            data.save()
            response_data = {
                "status" : "success",
                "message" : "Board update successfully",
                "data" : data.data
            }
            return Response(response_data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=['Board'],
    )
    def delete(self, request, pk=None):
        '''
        delete board
        '''
        board = get_object_or_404(Board, pk=pk)
        board.delete()
        response_data = {
            "status" : "success",
            "message" : "board deleted successfully",
        }
        return Response(response_data,status=status.HTTP_204_NO_CONTENT)

    
#card views
class CardApiView(APIView):
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        '''
        Get card List
        '''
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        response_data = {
            "status" : "success",
            "message" : " List of card retrieved successfully",
            "data" : serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
         Post data
         '''
        cards = CardSerializer(data=request.data)
        if cards.is_valid():
            cards.save()
            response_data = {
                "status" : "success",
                "message" : "card saved successfully",
                "data" : cards.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CardDetailApiView(APIView):
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated,)

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
                response_data = {
                    "status" : "success",
                    "message" : "card retrieved successfully",
                    "data" : serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
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
            response_data = {
                "status" : "success",
                "message" : "card updated successfully",
                "data" : data.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete card
        '''
        card = get_object_or_404(Card, pk=pk)
        card.delete()
        response_data = {
            "status" : "success",
            "message" : "card deleted successfully",
        }
        return Response(response_data,status=status.HTTP_204_NO_CONTENT)


#Task views
class TaskApiView(APIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        '''
        Get Task List
        '''
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        response_data = {
            "status" : "success",
            "message" : "List of task retrieved successfully",
            "data" : serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
         Post Task data
         '''
        tasks = TaskSerializer(data=request.data)
        if tasks.is_valid():
            tasks.save()
            response_data = {
                "status" : "success",
                "message" : "task saved successfully",
                "data" : tasks.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
class TaskDetailApiView(APIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    
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
                response_data = {
                    "status" : "success",
                    "message" : "task retrieved successfully",
                    "data" : serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
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
            response_data = {
                "status" : "success",
                "message" : "task updated successfully",
                "data" : data.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete Task
        '''
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        response_data = {
            "status" : "success",
            "message" : "task deleted successfully",
        }
        return Response(response_data,status=status.HTTP_204_NO_CONTENT)


#Activity views
class ActivityApiView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        '''
        Get Activity List
        '''
        activitys = Activity.objects.all()
        serializer = ActivitySerializer(activitys, many=True)
        response_data = {
            "status" : "success",
            "message": "List of activity retrieved  successfully",
            "data" : serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
         Post  Activity data
         '''
        data = {}

        activitys = ActivitySerializer(data=request.data)
        if activitys.is_valid():
            activitys.save()
            response_data = {
                "status" : "success",
                "message" : "activity saved successfully",
                "data" : activitys.data
            }
            return Response(response_data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
class ActivityDetailApiView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = (IsAuthenticated,)
    
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
                response_data = {
                    "status" : "success",
                    "message" : "activity retrieved successfully",
                    "data" : serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
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
            response_data = {
                "status" : "success",
                "message" : "activity updated successfully",
                "data" : data.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete Activity
        '''
        activity = get_object_or_404(Activity, pk=pk)
        activity.delete()
        response_data = {
            "status" : "success",
            "message" : "activity deleted successfully",
        }
        return Response(response_data,status=status.HTTP_202_ACCEPTED)


#Job views
class JobApiView(APIView):
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        '''
        Get Job List
        '''
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        response_data = {
            "status" : "success",
            "message" : "List of job retrieved successfully",
            "data" : serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Post  Job data
        '''
        random_uuid = uuid.uuid1()
        print("1111")
        job_id = str(random_uuid)
        print("222222")
        while Job .objects.filter(job_id=random_uuid).exists():
            print("33333333")
            random_uuid = uuid.uuid1()
            print("44444444444444")
        data = {
            "job_id" : request.data.get("job_id"),
            "job_title" : request.data.get("job_title"),
            "description" : request.data.get("decription"),
        }
        print("555555555555")
        jobs = JobSerializer(data=request.data)
        if jobs.is_valid():
            jobs.save()
            response_data = {
                "status" : "success",
                "message" : "job saved successfully",
                "data" : jobs.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class JobDetailApiView(APIView):
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)

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
                response_data = {
                    "status" : "success",
                    "message" : "job retrieved successfully",
                    "data": serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
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
            response_data = {
                "status" : "success",
                "message" : "job updated successfully",
                "data" : data.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete job
        '''
        job = get_object_or_404(Job, pk=pk)
        job.delete()
        response_data = {
            "status" : "success",
            "message" : "job deleted successfully",
        }
        return Response(response_data,status=status.HTTP_204_NO_CONTENT)


class InterviewerApiView(APIView):
    serializer_class = InterviewerSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        '''
        Get Interviewer List
        '''
        interviewers = Interviewer.objects.all()
        serializer = InterviewerSerializer(interviewers, many=True)
        response_data = {
            "status" : "success",
            "message" : "List of interviewer retrieved successfully",
            "data" :serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        post interviewer data
        '''
        data = {}
        interviewers = InterviewerSerializer(data=request.data)
        if interviewers.is_valid():
            interviewers.save()
            response_data = {
                "status" : "success",
                "message" : "interviewer saved successfully",
                "data" : interviewers.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
class InterviewerImportAPI(APIView):
    serializer_class = InterviewerSerializer1

    def post(self, request, *args, **kwargs):
        company_id = request.data.get('company', None)
        file = request.FILES.get('file')

        if not file:
            return Response({"error": "please provide Excel file."}, status=status.HTTP_400_BAD_REQUEST)

        if not company_id:
            return Response({"error":"please provide valid company_id."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            if not file.name.endswith('.xlsx'):
                return Response({"error" : "Invalid file format,only excel file are supported."}, status= status.HTTP_400_BAD_REQUEST)
            else:
                df = pd.read_excel(file)
                for index, row in df.iterrows():
                    try:
                        data = row.to_dict()
                        data["company_id"] = int(company_id)
                        serializer = InterviewerSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            response_data = {
                                "status" : "success",
                                "message" : "interviewer imported successfully",
                                "data" : serializer.data
                            }
                        else:
                            print("serializer.errors : ", serializer.errors)
                        # interviewer_obj = Interviewer.objects.create(**row.to_dict())
                    except:
                        print("error : ", row.to_dict)
                return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            


class InterviewerDetailApiView(APIView):
    serializer_class = InterviewerSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        '''
        get single interviewer
        '''
        if pk:
            try:
                interviewer = Interviewer.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if interviewer:
                serializer = InterviewerSerializer(interviewer)
                response_data = {
                    "status" : "success",
                    "message" : "interviewer retrieved succesfully",
                    "data" : serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        '''
        update interviewer
        '''
        interviewer = Interviewer.objects.get(pk=pk)
        data = InterviewerSerializer(instance=interviewer, data=request.data)
        if data.is_valid():
            data.save()
            response_data = {
                "status" : "success",
                "message" : "interviewer updated successfully",
                "data" : data.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request,pk=None):
        '''
        delete interviewer
        '''
        interviewer = get_object_or_404(Interviewer,pk=pk)
        interviewer.delete()
        response_data = {
            "status" : "success",
            "message" : "interviewer deleted successfully",
        }
        return Response(response_data,status=status.HTTP_204_NO_CONTENT)









    







 

    


    


    







    




  



    

    
    


    


        
        





