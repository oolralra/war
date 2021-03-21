from .models import User
from rest_framework import serializers

class SignupSerializer(serializers.ModelSerializer):
    pwd = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'user_index',
            'user_id',
            'pwd',
            'user_type',
            'user_name',
            'auth_code',
            'user_email',
            'phone_number',
            'birth_day',
            'pwd_modified_at',
            'created_at',
            'modified_at'
        ]