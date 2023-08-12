from rest_framework import serializers
from .models import Company,  Subscription, CompanySubscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["plan", "amount"]


class CompanySerializer(serializers.ModelSerializer):
    

    def create(self, validated_data):
        validated_data["user"] = self.context.get('user', None)
        subscription_id = self.context.get('subscription_id', None)

        company = Company.objects.create(**validated_data)

        if company and subscription_id:
            subscription_data = {
                "subscription_id": subscription_id,
                "company": company.id,
                "status": True
            }
            CompanySubscription.objects.create(**subscription_data)
        return company

    class Meta:
        model = Company
        fields = ['name', 'address', 'designation', 'email', 'mobile_number', 'gst_number', 'established_date', 'about', 'terms_policy', "Company_logo", 'created_at', 'modified_at',]


class CompanySubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanySubscription
        fields = ["status", "company", "subscription"]


