from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = models.User.objects.create(
            user_id=validated_data['user_id'],
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            birth_day=validated_data['birth_day']
        )
        password = make_password(validated_data['password'])
        user.password = password
        user.save()
        return user

    class Meta:
        model = models.User
        fields = [
            'user_index',
            'user_id',
            'password',
            'username',
            'email',
            'phone_number',
            'birth_day',
            'pwd_modified_at',
            'created_at',
            'modified_at'
        ]