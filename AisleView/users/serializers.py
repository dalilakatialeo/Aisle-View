from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser(
            first_name= validated_data["first_name"],
            last_name= validated_data['last_name'],
            email= validated_data["email"],
            username= validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

#update user details - name and email

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance