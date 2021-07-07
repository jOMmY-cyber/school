from django.urls import path, include
from .views import *
from .api import *
from import *
import server.apis_on_chain as apis_on_chain
urlpatterns = [
    path('user-profile/', APIProfile.as_view()),
    path('student/',APIStudents.as_view()),
    path('room/'APIRoom.as_view()),
    
]
