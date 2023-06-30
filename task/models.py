from django.db import models


# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length = 200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default=False, null=False)
    card_name = models.CharField(max_length=200, blank=False, null=False)
    sequence = models.IntegerField(default=0,blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True,blank=False, null=False)
    modified_at = models.DateTimeField(auto_now=True,blank=False, null=False)

    def __str__(self):
        return self.card_name


class Task(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, default=False, null=False)
    task_name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name


class Activity(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, default=False, null=False)
    comment =models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class ActivityFile(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, default=False, null=False)
    file = models.FileField(upload_to = "media/images/activity", default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



