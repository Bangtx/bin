from importlib.resources import path

from django.contrib import admin
from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index().login_register, name='login'),
    path('ad', Index().admin, name='admin'),
    path('edit/<int:id>', Index().edit_user, name='edit'),
    path('delete/<int:id>', Index().delete_user, name='delete'),
    path('add_user', Index().add_user, name='add_user')
]
