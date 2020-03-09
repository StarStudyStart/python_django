#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/7 0007 18:17
"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users import views

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', redirect_field_name='my_redirect_field'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
