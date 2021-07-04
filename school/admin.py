from django.contrib import admin
from .models import *

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'level', 'is_invited_by']

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['code']

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['code']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['code']

@admin.register(Parents)
class ParentsAdmin(admin.ModelAdmin):
    list_display = ['code']

@admin.register(Phone_number)
class Phone_numberAdmin(admin.ModelAdmin):
    list_display = ['code']
