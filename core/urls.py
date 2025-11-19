"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from conversor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'), 
]