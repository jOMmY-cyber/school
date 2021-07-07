from django.core.checks.messages import ERROR
from .models import *
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
import rest_framework.permissions as rfperm
from rest_framework.authtoken.models import Token
import json

from .serializers import *
from myschool.utils import *
from django.utils.crypto import get_random_string

class APIProfile(APIView):
    model = UserProfile
    serializer = UserProfileSerializer
    def get(self, request, *args, **kwargs):
        try:
            data = request.GET.dict()
            obj = self.model.objects.filter(**data)
            serializer = self.serializer(obj, many=True)
            return Response(serializer.data, status=200)
        except:
            return Response('fail', status=400)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            act = data['act']
            dat = data['detail']
            try:
                if act == 'create':
                    username = dat.pop('username')
                    password = dat.pop('password')
                    users = User.objects.filter(username=username)
                    if users.exists():
                        return Response('duplicated username', status=400)
                    new_user = User.objects.create_user(username=username, password=password)
                    new_user.save()


                    serializer = self.serializer(data=dat, many=False)
                    if serializer.is_valid():
                        serializer.save(
                            user = new_user,
                            code = 'register',
                            created_by_username = new_user.username,
                            updated_by_username = new_user.username,
                            is_active = True,
                            created_on = timezone.now(),
                        )
            except Exception as e:
                try:
                    new_user.delete()
                except:pass

                return Response('Unable to create! '+str(e), status=400)


            try:
                if act == 'update':
                    obj = self.model.objects.get(user=request.user)
                    serializer = self.serializer(obj, data=dat)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=201)
                    else:
                        return Response(serializer.errors, status=400)
            except Exception as e:
                return Response('Unable to update! '+str(e), status=400)
        
        except:
            return Response('failed have no act or detail', status=400)
class APIStudents(APIView):
    model = UserProfile
    serializer = UserProfileSerializer
    def get(self, request, *args, **kwargs):
        try:
            data = request.GET.dict()
            obj = self.model.objects.filter(**data)
            serializer = self.serializer(obj, many=True)
            return Response(serializer.data, status=200)
        except:
            return Response('fail', status=400)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            act = data['act']
            dat = data['detail']
            try:
                if act == 'create':
                    username = dat.pop('username')
                    password = dat.pop('password')
                    users = User.objects.filter(username=username)
                    if users.exists():
                        return Response('duplicated username', status=400)
                    new_user = User.objects.create_user(username=username, password=password)
                    new_user.save()


                    serializer = self.serializer(data=dat, many=False)
                    if serializer.is_valid():
                        serializer.save(
                            user = new_user,
                            code = 'register',
                            created_by_username = new_user.username,
                            updated_by_username = new_user.username,
                            is_active = True,
                            created_on = timezone.now(),
                        )
            except Exception as e:
                try:
                    new_user.delete()
                except:pass

                return Response('Unable to create! '+str(e), status=400)


            try:
                if act == 'update':
                    obj = self.model.objects.get(user=request.user)
                    serializer = self.serializer(obj, data=dat)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=201)
                    else:
                        return Response(serializer.errors, status=400)
            except Exception as e:
                return Response('Unable to update! '+str(e), status=400)
        
        except:
            return Response('failed have no act or detail', status=400)
class APIRoom(APIView):
    model = UserProfile
    serializer = UserProfileSerializer
    def get(self, request, *args, **kwargs):
        try:
            data = request.GET.dict()
            obj = self.model.objects.filter(**data)
            serializer = self.serializer(obj, many=True)
            return Response(serializer.data, status=200)
        except:
            return Response('fail', status=400)

    def post(self, request, *args, **kwargs):
        data = request.data
        act = data.get('act')
        detail = data.get('detail')
        if act == None:
            return Response('........................',status = 400)
        if detail == None:
            return Response('-------------------------',status = 400)
        if data == int:
            return Response('------------------',status = 400)
        if act == 'create':
            market_group = super().get_chain(request)
            serializer = self.serializer(data = detail,many=False)
            if serializer.is_valid():
                new = serializer.save(
                    market_group = market_group,
                    created_by_username = request.user.username,
                    updated_by_username = request.user.username,
                    created_on = timezone.now(),
                )
                print(request.user.username)
                return Response(serializer.data,status=200)
            if serializer.is_valid():
                new_user = request.user

class APIParents(models.Models):