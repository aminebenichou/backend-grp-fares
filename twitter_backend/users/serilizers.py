from rest_framework import serializers
from .models import customuser
from django.contrib.auth.models import Group, Permission

class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model= customuser
        fields='__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Correct way: use set_password or create_user
        user = customuser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'] # This will be hashed
        )

        return user
    


class groupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group 
        fields='__all__'

class permissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permission 
        fields='__all__'