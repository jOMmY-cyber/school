from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
import datetime
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
import copy
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from server.models import *
############ functions ###########
def clone(instance):
    cloned = copy.copy(instance) # don't alter original instance
    cloned.pk = None
    try:
        delattr(cloned, '_prefetched_objects_cache')
    except AttributeError:
        pass
    return cloned

def exclusive_tax(service_charge_rate, tax_rate, revenue):
    service_charge = revenue * service_charge_rate/100
    tax = revenue * tax_rate/100
    total = revenue + service_charge + tax
    return service_charge, tax, total

def inclusive_tax(service_charge_rate, tax_rate, revenue):
    service_charge = revenue - (revenue / (service_charge_rate/100 + 1))
    tax = revenue / (tax_rate/100 + 1)
    total = revenue
    return service_charge, tax, total

############# forms #######################
class DateInput(forms.DateInput):
    input_type = 'date'
class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'
class PasswordInput(forms.PasswordInput):
    input_type = 'password'
    


################ views #############################
class BaseView(View):
    context = {}
    def render(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    def login(self, request, *args, **kwargs):
        user = authenticate(username=request.POST.get('email'),
                            password=request.POST.get('password'),)
        if user is not None:
            login(request, user)
            return True
        return False
    def perm(self, request, *args, **kwargs):
        # check authen level
        if not request.user.is_authenticated:
            print('user is not authenticated')
            messages.warning(request, 'please login')
            logout(request)
            return
        
        # check no level user
        # try:
        #     request.user.userprofile.level
        # except:
        #     print('user has no level')
        #     messages.warning(request, 'user has no level')
        #     return
        
        # check permission
        # 1 => highest
        # 2 => lower
        # 3 => lower
        # you have to solve this 
        # if request.user.userprofile.level > self.permission:
        #     print('user has no permission')
        #     messages.warning(request, 'user has no permission')
        #     return # allow <=
        
        # check has permission in this property or not
        print('warning from sk, you have to solve this line')
        
        self.get_chain(request, *args, **kwargs)
        return True
    
    def get_chain(self, request, *args, **kwargs):
        profile = UserProfile.objects.get(user=request.user)
        big_boss_username = profile.big_boss_username
        print('big', big_boss_username)
        return None
    def get_chain_property(self, pk):
        if pk is None:
            return None
        self.chain_property = ChainProperty.objects.get(pk=pk)
        return self.chain_property
    
    def message(self):
        request = 'comment'
        # add message
        messages.warning(request, 'Your account expires in three days.')
        
        # get message
        from django.contrib.messages import get_messages
        storage = get_messages(request)
        for message in storage:
            print('message', message)
            
def handle_uploaded(request, fieldname):
        file_image = request.FILES[fieldname]
        file_image_name = request.FILES[fieldname].name.replace(" ", "")
        fs = FileSystemStorage()
        filename = fs.save(file_image_name, file_image)
        upload_file_url = fs.url(filename)
        return upload_file_url[6:]

class MyAPIView(APIView):
    def has_perm(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return True
        
        # get user level
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            profile_level = user_profile.level
        except:
            return False

        if self.permission_level < profile_level:
            return False

        return True

    def is_valid_fields(self, data):
        field_names = [field.name for field in self.model._meta.get_fields()]
        for element in data:  # dat.type == list
            for key, value in element.items():
                if key not in field_names:
                    return False
        return True

    def get_chain(self, request, *args, **kwargs):
        profile = UserProfile.objects.get(user=request.user)
        big_boss_username = profile.big_boss_username
        big_boss = User.objects.get(username=big_boss_username)
        chain = Chain.objects.get(user=big_boss)

        return chain
    
    def get_property(self, request):
        chain = self.get_chain(request)
        properties = ChainProperty.objects.filter(chain=chain)
        profile = UserProfile.objects.get(user=request.user)
        current_property = profile.current_property
        if current_property == None:
            return properties.first()
        else:
            return properties.get(pk=current_property.pk)
