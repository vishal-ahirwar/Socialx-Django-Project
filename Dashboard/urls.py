from django.urls import path
from .views import *
app_name='Dashboard'

urlpatterns=[
    path('',Home,name='home'),
]