from django.db import models
from django.contrib.auth.models import User
from company.models import Company

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="users", on_delete=models.CASCADE, blank=False, null=False)


class Hr(models.Model):
    user = models.OneToOneField(User, related_name="hr_users", on_delete=models.CASCADE, blank=False, null=False)
    company = models.ForeignKey(Company, related_name="company_name", on_delete=models.CASCADE, blank=False, null=False)


class Candidate(models.Model):
    user = models.OneToOneField(User, related_name="candidate", on_delete=models.CASCADE, blank=False, null=False)


class CompanysCandidates(models.Model):
    company = models.OneToOneField(Company, related_name="company_candidate", on_delete = models.CASCADE, blank=False, null=False)
    candidate = models.ManyToManyField(Candidate, related_name="candidate_company")