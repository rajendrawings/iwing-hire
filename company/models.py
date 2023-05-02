from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length = 180)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name