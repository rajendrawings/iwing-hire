from django.db import models
from django.utils import timezone
from company.models import Company



class Board(models.Model):
    name = models.CharField(max_length = 200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    board = models.ForeignKey(Board, related_name='cards', on_delete=models.CASCADE, default=False, null=False)
    card_name = models.CharField(max_length=200, blank=False, null=False)
    sequence = models.IntegerField(default=0,blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True,blank=False, null=False)
    modified_at = models.DateTimeField(auto_now=True,blank=False, null=False)

    def __str__(self):
        return self.card_name


class Task(models.Model):
    card = models.ForeignKey(Card,related_name='tasks', on_delete=models.CASCADE, default=False, null=False)
    task_name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name


class Activity(models.Model):
    task = models.ForeignKey(Task, related_name='activitys', on_delete=models.CASCADE, default=True, null=True)
    comment =models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to = "media/images/activity", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class Job(models.Model):
    job_title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_title


class Interviewer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100, blank = False)
    designation = models.CharField(max_length=100, blank=True, null=True)
    skill_sets = models.CharField(max_length=100, blank=True, null=True)
    year_of_experience = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="media/images/activity", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    










