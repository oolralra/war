from django.db import models

class User(models.Model):
    user_index = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=150)
    username = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    birth_day = models.CharField(max_length=10, blank=True, null=True)
    pwd_modified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
