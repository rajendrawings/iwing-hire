from django.db import models
from django.contrib.auth.models import User
from company.models import Company
import uuid
from django.utils import timezone
# from profiles.models import HRGroup




class Profile(models.Model):
    user = models.OneToOneField(User, related_name="users", on_delete=models.CASCADE, blank=False, null=False)


class HRGroup(models.Model):
    group_id = models.UUIDField(default=uuid.uuid4 )
    group_name = models.CharField(max_length=100 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group_name


class Hr(models.Model):
    user = models.OneToOneField(User, related_name="hr_users", on_delete=models.CASCADE, blank=False, null=False)
    company = models.ForeignKey(Company, related_name="company_name", on_delete=models.CASCADE, blank=False, null=False)
    email = models.EmailField(max_length=20, blank = True, null = True)
    mobile_number= models.IntegerField(blank=True, null=True)
    designation = models.CharField(max_length=200, blank = True, null = True)
    preposting_person_name= models.CharField(max_length=100, blank = True, null = True)
    groups = models.ManyToManyField(HRGroup, related_name="Group_field", blank=True)
    profile_pic = models.FileField(upload_to='media/images/activity', null=True)


class Candidate(models.Model):
    user = models.OneToOneField(User, related_name="candidate", on_delete=models.CASCADE, blank=False, null=False)


class CompanysCandidates(models.Model):
    company = models.OneToOneField(Company, related_name="company_candidate", on_delete = models.CASCADE, blank=False, null=False)
    candidate = models.ManyToManyField(Candidate, related_name="candidate_company")


