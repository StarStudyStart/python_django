#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/11 0011 20:55
"""
from django.urls import path
from bg_management import views

app_name = 'bgm'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('<str:app_name>/<str:table_name>/', views.model_list, name='model_list'),
    path('<str:app_name>/<str:table_name>/<int:id>/change/', views.model_list_change, name='model_list_change')
]
