#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/11 0011 20:58
"""
from crm import models

enabled_admins = {}


class BaseAdmin(object):
    list_display = []
    list_filter = []
    list_per_page = 1


class CustomerAdmin(BaseAdmin):
    list_display = ['id', 'name', 'qq_number', 'referral', 'date', 'status']
    list_filter = ['name', ]


def register(model_class, admin_class=None):
    app_name = model_class._meta.app_label
    model_name = model_class._meta.model_name
    if app_name not in enabled_admins:
        enabled_admins[app_name] = {}
    admin_class.model = model_class
    enabled_admins[app_name][model_name] = admin_class


register(models.Customer, CustomerAdmin)
