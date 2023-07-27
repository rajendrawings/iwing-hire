from rest_framework import serializers
from .models import Company, CompanyLogo, Subscription

class CompanyLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyLogo
        fields = ["file", "company"]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["plan", "amount"]


class CompanySerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)
    subscription = SubscriptionSerializer()
    class Meta:
        model = Company
        fields = ['name', 'subscription',  'file']





