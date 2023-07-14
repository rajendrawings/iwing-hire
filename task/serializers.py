from django.db.models import fields
from rest_framework import serializers
from .models import Board, Card, Task, Activity


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
        fields= ('id', 'board', 'card_name', 'sequence')


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








