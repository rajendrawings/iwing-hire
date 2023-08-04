from django.db.models import fields
from rest_framework import serializers
from .models import Board, Card, Task, Activity, Job, Interviewer
from company.serializers import CompanySerializer
import odf
import pandas as pd



#serializer for activity
class ActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Activity
        fields = ('id', 'task', 'file', 'comment')


class GetActivitySerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)
    
    class Meta:
        model = Activity
        fields = ('id', 'task', 'file', 'comment')


#serializer for only for task data
class TaskSerializer(serializers.ModelSerializer):                                                                                                                                                                                                                                              
    
    class Meta:
        model = Task
        fields = ('id', 'card', 'task_name', 'description')


#serializer for get task with activity list
class GetTaskSerializer(serializers.ModelSerializer):
    activitys = ActivitySerializer(many=True)
    
    class Meta:
        model = Task
        fields = ('id', 'card', 'activitys', 'task_name', 'description')


#serializers only for card data
class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Card
        fields= ('id', 'board', 'tasks', 'card_name', 'sequence')


#serializer for get card with task list
class GetCardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    
    class Meta:
        model= Card
        fields= ('id', 'board', 'tasks', 'card_name', 'sequence')


#serializer only for board data
class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ('id', 'name', 'cards', 'created_at', 'modified_at')


#serializer for get board with card list
class GetBoardSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'cards', 'created_at', 'modified_at')


#serializer for Job
class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'job_title', 'description', 'created_at', 'modified_at')


#serializer for Interviewer
class InterviewerSerializer(serializers.ModelSerializer):
    # company = CompanySerializer(many=True)

    class Meta:
        model = Interviewer
        fields = ('id', 'name', 'first_name', 'last_name', 'email', 'designation', 'skill_sets', 'year_of_experience', 'employee_id', 'created_at', 'modified_at')


class InterviewerSerializer1(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Interviewer
        fields = ('file', 'company')









