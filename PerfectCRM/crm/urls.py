#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/11 0011 20:33
"""

from django.urls import path
from crm import views

app_name = 'crm'
urlpatterns = [
    path('index/', views.index, name='index')
]
