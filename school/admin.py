from django.contrib import admin
from .models import *

@admin.register(InvitationLink)
class InvitationLinkAdmin(admin.ModelAdmin):
    list_display = ['code', 'url']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'level', 'is_invited_by']

@admin.register(School)
class ChainAdmin(admin.ModelAdmin):
    list_display = ['code']

@admin.register(Students)
class MarketGroupAdmin(admin.ModelAdmin):
    list_display = ['code']

@admin.register(Room)
class MarketSegmentAdmin(admin.ModelAdmin):
    list_display = ['code']

@admin.register(Parents)
class StandardRateCodeAdmin(admin.ModelAdmin):
    list_display = ['code']

@admin.register(Phone_number)
class RevenueGroupAdmin(admin.ModelAdmin):
    list_display = ['code']
