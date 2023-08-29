from django.contrib import admin
from .models import Company, Subscription, CompanySubscription

admin.site.register(Company)
admin.site.register(Subscription)
admin.site.register(CompanySubscription)


