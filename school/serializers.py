from .models import *
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'middle_name', 'last_name', 'gender', 'date_of_birth', 'phone_number', 'department')

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('code', 'description')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ParentsCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = '__all__'

class Phone_numberGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone_number
        fields = '__all__'