#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/14 0014 16:52
"""
from django.db.models import Q


def after_filter(request, admin_class):
    """返回过滤后的数据，以及过滤条件"""
    filter_conditions = {}
    keywords = ['page', '_q', 'o']
    for k, v in request.GET.items():
        if k in keywords:  # 保留关键字
            continue
        if v:
            filter_conditions[k] = v

    return admin_class.model.objects.filter(**filter_conditions), filter_conditions


def after_search(request, model_lists, after_filter_lists):
    """过滤搜索后的数据"""
    query = request.GET.get("_q", "")
    if query:
        q = Q()
        q.connector = "OR"
        for column in after_filter_lists.search_fields:
            q.children.append(("%s__contains" % column, query))
        model_lists = model_lists.filter(q)
    return model_lists
