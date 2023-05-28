from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    role = models.CharField(max_length = 180, unique=True)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="users", on_delete=models.CASCADE, blank=False, null=False)
    role = models.OneToOneField(Role, related_name="roles", on_delete=models.CASCADE, blank=True, null=True)
