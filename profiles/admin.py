from .models import Profile, Hr, Candidate, CompanysCandidates, HRGroup
from django.contrib import admin

admin.site.register(Profile)
admin.site.register(Hr)
admin.site.register(Candidate)
admin.site.register(CompanysCandidates)

# for Hr_Group
admin.site.register(HRGroup)