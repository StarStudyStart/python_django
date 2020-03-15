#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/11 0011 20:58
"""
from crm import models
from django.contrib.auth.models import User

enabled_admins = {}


class BaseAdmin(object):
    list_display = []
    list_filters = []
    search_fields = ['id']
    list_per_page = 1


class CustomerAdmin(BaseAdmin):
    list_display = ['id', 'name', 'qq_number', 'referral', 'consultant', 'date', 'status']
    list_filters = ['name', 'referral', 'qq_number', 'status', 'consultant']
    search_fields = ['name', 'qq_number','consultant__user__username']


class UserAdmin(BaseAdmin):
    list_display = ['id', 'username', 'email', ]
    list_filters = ['id', 'username', ]


def register(model_class, admin_class=None):
    app_name = model_class._meta.app_label
    model_name = model_class._meta.model_name
    if app_name not in enabled_admins:
        enabled_admins[app_name] = {}
    admin_class.model = model_class
    enabled_admins[app_name][model_name] = admin_class


register(models.Customer, CustomerAdmin)
register(User, UserAdmin)
