import os
from datetime import timedelta, datetime
from rest_framework import status, generics, exceptions as exc
from rest_framework.response import Response

from . import serializers, models
import jwt
from django.contrib.auth.hashers import check_password


class SignView(generics.CreateAPIView):
    model = models.User
    serializer_class = serializers.SignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)

        return Response({
            'success': 1,
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)