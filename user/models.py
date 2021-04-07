# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    user_index = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    pwd = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50)
    auth_code = models.CharField(max_length=20, blank=True, null=True)
    user_email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    birth_day = models.CharField(max_length=10, blank=True, null=True)
    pwd_modified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

    # def indexing(self):
    #     obj = User(
    #         meta={'id': self.id},
    #         user_index=self.user_index,
    #         user_id=self.user_id,
    #         user_type=self.user_type,
    #         user_name=self.user_name,
    #         user_email=self.user_email,
    #         phone_number=self.phone_number,
    #         birth_day=self.birth_day,
    #         created_at=self.created_at,
    #         modified_at=self.modified_at,
    #     )
    #     obj.save()
    #     return obj.to_dict(include_meta=True)
