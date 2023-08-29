from rest_framework import serializers
from .models import Profile, Hr, Candidate, CompanysCandidates, HRGroup
from .common import create_user
from company.serializers import CompanySerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class GetProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ["user"]


class GetHrSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()

    class Meta:
        model = Hr
        fields = ["user", "company","email","mobile_number","designation","preposting_person_name","hr_groups", "profile_pic"]


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def create(self, validated_data):

        instance = create_user(validated_data)
        
        if instance:
            profile_data = {
                "user_id": instance.id,
            }
            profile = Profile.objects.create(**profile_data)
        return instance
    
    class Meta:
        model = Profile
        fields = ["email", "password", "confirm_password"]


class HrSerializer(serializers.ModelSerializer):
    def create(self, validated_data):

        instance = create_user(validated_data)
        
        if instance:
            hr_data = {
                "user": instance,
                "company": validated_data.get("company", ""),
                "email": validated_data.get('gmail'),
                "mobile_number": int(validated_data.get('mobile_number')),
                "designation": validated_data.get('designation'),
                "preposting_person_name": validated_data.get('preposting_person_name'),
                "profile_pic": validated_data.get('profile_pic'),
            }
            hr = Hr.objects.create(**hr_data)
            if hr:
                hr.groups.add(validated_data.get('groups')[0].id)
            return hr
    
    class Meta:
        model = Hr
        fields = ["id", "company","email","mobile_number", "designation", "preposting_person_name", "groups"]


class CandidateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    company = serializers.IntegerField()

    def create(self, validated_data):

        instance = create_user(validated_data)
        
        if instance:
            candidate_data = {
                "user_id": instance.id
            }
            candidate = Candidate.objects.create(**candidate_data)
            company_candidate_obj = CompanysCandidates.objects.filter(company_id=int(validated_data.get("company", ""))).first()
            if not company_candidate_obj:
                company_candidate_obj = CompanysCandidates.objects.create(company_id=int(validated_data.get("company", "")))
            company_candidate_obj.candidate.add(candidate)
        return instance
    
    class Meta:
        model = Candidate
        fields = ["email", "password", "confirm_password", "company"]


class GetCandidateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Candidate
        fields = ["user"]


class HRGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = HRGroup
        fields = ["id", "group_id", "group_name", "created_at", "modified_at"]
        