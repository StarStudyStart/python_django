#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/14 0014 11:44
"""
from django import template
from django.utils.html import format_html, mark_safe

register = template.Library()


@register.simple_tag
def get_verbose_name(model):
    return model._meta.verbose_name_plural


@register.simple_tag
def build_table_rows(obj, admin_class):
    row_ele = ""
    for column in admin_class.list_display:
        field_obj = obj._meta.get_field(column)
        if field_obj.choices:
            column_data = getattr(obj, 'get_%s_display' % column)()
        else:
            column_data = getattr(obj, column)
        if type(column_data).__name__ == 'datetime':
            column_data = column_data.strftime("%Y-%m-%d %H:%M:%S")
        row_ele += "<td>%s</td>" % column_data
    return format_html(row_ele)


@register.simple_tag
def render_page_ele(loop_counter, model_pages, filter_conditions):
    filter = ""
    for k, v in filter_conditions.items():
        if v:
            filter += '&%s=%s' % (k, v)
    if abs(model_pages.number - loop_counter) <= 1:
        ele_class = ""
        if model_pages.number == loop_counter:
            ele_class = "active"
        ele = '''<li class="%s"><a href="?page=%s&%s">%s</a></li>''' % (ele_class, loop_counter, filter, loop_counter)

        return mark_safe(ele)

    return ''


@register.simple_tag
def return_field_verbose_name(admin_class, filed_name):
    verbose_name = admin_class.model._meta.get_field(filed_name).verbose_name
    return verbose_name
