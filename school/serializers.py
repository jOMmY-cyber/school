from .models import *
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'middle_name', 'last_name', 'gender', 'date_of_birth', 'phone_number', 'department')

# class GivePermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GivePermission
#         fields = 'url', 'level','updated_on', 'is_active'

# #### chain
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('code', 'description')

# class ChainPropertySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ChainProperty
#         exclude = ('chain', 'is_active','id')

# class BedTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BedType
#         exclude = ('chain_property', 'created_by', 'updated_by', 'id')

# class ExposureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Exposure
#         exclude = ('chain_property', 'created_by', 'updated_by', 'id')

# class ZoneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Zone
#         exclude = ('chain_property', 'created_by', 'updated_by', 'id')
# class AttributeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attribute
#         exclude = ('chain_property', 'created_by', 'updated_by', 'id')
# class BuildingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Building
#         exclude = ('chain_property', 'created_by', 'updated_by', 'id')
# class FloorSerializer(serializers.ModelSerializer):
#     building_code = serializers.SerializerMethodField('_building_code')
#     def _building_code(self, obj):
#         return obj.building.code
    
#     class Meta:
#         model = Floor
#         exclude = ('building', 'created_by', 'updated_by', 'id')

# class RoomSerializer(serializers.ModelSerializer):
#     building_code = serializers.SerializerMethodField('_building_code')
#     floor_code = serializers.SerializerMethodField('_floor_code')
#     def _building_code(self, obj):
#         return obj.floor.building.code
#     def _floor_code(self, obj):
#         return obj.floor.code
    
#     class Meta:
#         model = Room
#         exclude = ('floor', 'created_by', 'updated_by', 'id')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
        # exclude = ('chain_obj','id','created_by_username','updated_by_username')

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