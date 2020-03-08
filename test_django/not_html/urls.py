#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/7 0007 10:46
"""
from django.urls import path
from not_html import views

urlpatterns = [
    path('image/', views.my_image, name='my_image'),
    path('csv/', views.my_csv, name='my_csv'),
    path('pdf/', views.my_pdf, name='my_csv'),
]
