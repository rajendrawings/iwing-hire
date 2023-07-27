from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Subscription(models.Model):
    PLAN_CHOICES = (
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    )

    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Company(models.Model):
    name = models.CharField(max_length = 180, unique=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    # subscription = models.ForeignKey(Subscription, on_delete = models.CASCADE, blank = True, null = True)
    address = models.CharField(max_length = 500, blank = True, null = True)
    designation = models.CharField(max_length = 200, blank = True, null = True)
    email = models.CharField(max_length=100, blank = True, null = True)
    mobile_no = models.IntegerField(blank = True, null = True)
    gst_no = models.IntegerField(blank = True, null = True)
    established_date = models.DateTimeField(timezone.now())
    about = models.CharField(max_length = 400, blank = True, null = True)
    terms_policy = models.CharField(max_length = 500, blank = True, null = True)
    


    def __str__(self):
        return self.name


class CompanyLogo(models.Model):
    file = models.FileField(upload_to = "media/images/activity", null=True)
    company = models.ForeignKey(Company, on_delete = models.CASCADE, blank = True, null = True)



