from rest_framework import serializers

from .models import Profile, Role
from django.contrib.auth.models import User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id", "role"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class GetProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    role = RoleSerializer()

    class Meta:
        model = Profile
        fields = ["user", "role"]


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        data = {
            "username": validated_data.get("email", ""),
            "email": validated_data.get("email", ""),
            "password": validated_data.get("password", "")
        }

        password = validated_data.pop('password', None)
        instance = User.objects.create(**data)
        
        # Adding the below line made it work for me.
        instance.is_active = True
        if password is not None:
            # Set password does the hash, so you don't need to call make_password 
            instance.set_password(password)
        instance.save()
        if instance:
            profile_data = {
                "user_id": instance.id,
                "role": validated_data.get("role", "")
            }
            profile = Profile.objects.create(**profile_data)
        return instance
    
    class Meta:
        model = Profile
        fields = ["email", "password", "role"]
