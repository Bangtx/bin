from importlib.resources import path

from django.contrib import admin
from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index().login_register, name='login')
]
