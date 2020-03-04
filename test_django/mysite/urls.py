#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabin
Time    : 2020/2/21 0021 17:58
"""
from django.urls import path, re_path

from mysite import views

app_name = 'mysite'
urlpatterns = [
    path("current_time/", views.get_current, name="current_time"),
    # re_path("(?P<year>[0-9]{1,2})/", views.get_current,name="current_time"),
    # path("<int:year>/", views.get_current,name="current_time"),
    # 显示请求头信息
    path("display_meta/", views.display_meta, name="display_meta"),
    # 表单请求
    path('search/', views.search, name='search'),
    path('search_results/<str:query>/', views.search_results, name='search_results'),
]
