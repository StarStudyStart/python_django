#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/4 0004 19:16
"""
from django.urls import path
from generic_view.views import PublisherList,PublisherDetail, BookList, PublisherBookList
urlpatterns = [
    path('publisher/list_view/', PublisherList.as_view()),
    path('book/list_view/', BookList.as_view()),
    path('book/<str:publisher>/', PublisherBookList.as_view()),
    path('publisher/detail_view/<int:pk>', PublisherDetail.as_view()),
]