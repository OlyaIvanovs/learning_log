"""Defines URL patterns for user"""

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # Registration path
    path('register/', views.register, name='register'),
]
