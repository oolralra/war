from django.db import models
from base.common.models import BaseModel


class User(BaseModel):
    user_index = models.AutoField(primary_key=True, verbose_name="회원번호")
    user_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=120)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    birth_day = models.CharField(max_length=10, blank=True, null=True)
    pwd_modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = "유저"
        app_label = "user"
