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
        column_data = ""
        if field_obj.choices:
            column_data = getattr(obj, 'get_%s_display' % column)()
        else:
            column_data = getattr(obj, column)
        if type(column_data).__name__ == 'datetime':
            column_data = column_data.strftime("%Y-%m-%d %H:%M:%S")
        row_ele += "<td>%s</td>" % column_data
    return format_html(row_ele)


@register.simple_tag
def render_page_ele(loop_counter, model_pages, filter_conditions, query):
    filter = ""
    for k, v in filter_conditions.items():
        if v:
            filter += '&%s=%s' % (k, v)
    if abs(model_pages.number - loop_counter) <= 1:
        ele_class = ""
        if model_pages.number == loop_counter:
            ele_class = "active"
        ele = '''<li class="%s"><a href="?page=%s&%s&_q=%s">%s</a></li>''' % (ele_class, loop_counter, filter, query,loop_counter)

        return mark_safe(ele)

    return ''


@register.simple_tag
def return_field_verbose_name(admin_class, filed_name):
    verbose_name = admin_class.model._meta.get_field(filed_name).verbose_name
    return verbose_name


@register.simple_tag
def render_filter_ele(condtion, admin_class, filter_condtions):
    select_ele = '''<select class="form-control" name='%s' ><option value=''>----</option>''' % condtion
    field_obj = admin_class.model._meta.get_field(condtion)
    selected = ''
    if field_obj.choices:
        for choice_item in field_obj.choices:
            print("choice", choice_item, filter_condtions.get(condtion), type(filter_condtions.get(condtion)))
            if filter_condtions.get(condtion) == str(choice_item[0]):
                selected = "selected"

            select_ele += '''<option value='%s' %s>%s</option>''' % (choice_item[0], selected, choice_item[1])
            selected = ''

    if type(field_obj).__name__ == "ForeignKey":
        for choice_item in field_obj.get_choices()[1:]:
            if filter_condtions.get(condtion) == str(choice_item[0]):
                selected = "selected"
            select_ele += '''<option value='%s' %s>%s</option>''' % (choice_item[0], selected, choice_item[1])
            selected = ''

    if type(field_obj).__name__ == "CharField":
        for obj in admin_class.model.objects.all():
            selected = ''

            option_value = getattr(obj, condtion)
            if filter_condtions.get(condtion) == str(option_value):
                selected = "selected"
            select_ele += '''<option value='%s' %s>%s</option>''' % (option_value, selected, option_value)

    select_ele += "</select>"
    return mark_safe(select_ele)
