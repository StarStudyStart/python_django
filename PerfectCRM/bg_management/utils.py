#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/14 0014 16:52
"""


def after_filter(request, admin_class):
    """返回过滤后的数据，以及过滤条件"""
    filter_conditions = {}
    for k, v in request.GET.items():
        if k=="page":#保留关键字
            continue
        if v:
            filter_conditions[k] = v

    return admin_class.model.objects.filter(**filter_conditions), filter_conditions
