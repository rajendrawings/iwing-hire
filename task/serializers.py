from django.db.models import fields
from rest_framework import serializers
from .models import Board, Card, Task, Activity


#serializer for Activity
class ActivitySerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)
    
    class Meta:
        model = Activity
        fields = ('id', 'task', 'file', 'comment')


#serializer for only for task data
class TaskSerializer(serializers.ModelSerializer):                                                                                                                                                                                                                                              
    
    class Meta:
        model = Task
        fields = ('id', 'card', 'activitys', 'task_name', 'description')


#serializer for get task with activity list
class GetTaskSerializer(serializers.ModelSerializer):
    activitys = ActivitySerializer(many=True)
    
    class Meta:
        model = Task
        fields = ('id', 'card', 'activitys', 'task_name', 'description')


#serializers for cards 
class CardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    
    class Meta:
        model= Card
        fields= ('id', 'board', 'tasks', 'card_name', 'sequence')


#serializer for board
class BoardSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'cards', 'created_at', 'modified_at')








