from django.test import TestCase, Client, tag
from .models import *
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import json
from uuid import UUID
