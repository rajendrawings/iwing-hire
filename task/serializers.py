from django.db.models import fields
from rest_framework import serializers
from .models import Board, Card, Task, Activity, ActivityFile
 
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name', 'created_at', 'modified_at')



#serializers for cards 

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields= ('id', 'board', 'card_name', 'sequence')

#serializer for Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'card', 'task_name', 'description')

#serializer for Activity
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'task', 'comment')

class ActivityFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    
    class Meta:
        model = ActivityFile
        fields = ('file', 'activity')
