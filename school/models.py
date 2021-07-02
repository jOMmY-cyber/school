from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

class MyModel(models.Model):
    id = models.CharField(max_length=25,primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, null=True, blank=True)
    created_by_username = models.CharField(max_length=255)
    updated_by_username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(self.code)

class School(MyModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Students(MyModel):
    students = models.ForeignKey(School, on_delete=models.CASCADE)

class Room(MyModel):
    room  = models.ForeignKey(Students, on_delete=models.CASCADE)

class Parents(MyModel):
    parents = models.ForeignKey(Students, on_delete=models.CASCADE)

class Phone_number(MyModel):
    phone_nubers = models.ForeignKey(Parents, on_delete=models.CASCADE)

class UserProfile(MyModel):
    user = models.OneToOneField(User, related_name="userprofileuser", on_delete=models.CASCADE)
    big_boss_username = models.CharField(max_length=255, null=True, blank=True)
    is_invited_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='userprofile/%Y/%m/%d/', null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)