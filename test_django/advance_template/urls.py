#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/3 0003 20:33
"""

from django.urls import path
from advance_template import views
app_name = 'advance_template'
urlpatterns = [
    path('1/', views.request_context_test1, name='request_context_test1'),
    path('2/', views.request_context_test2, name='request_context_test2'),
]