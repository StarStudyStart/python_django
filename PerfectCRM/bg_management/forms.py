#!/usr/bin/env python
# coding:utf-8
"""
Author  : yabinli
Time    : 2020/3/19 0019 20:40
"""
from django.forms import ModelForm
from crm import models


class CustomerModel(ModelForm):
    """顾客form表单"""

    class Meta:
        model = models.Customer
        fields = '__all__'


def create_model_form(admin_class):
    """动态构建form表单"""

    def __new__(cls, *args, **kwargs):
        # cls.base_fields['phone'].widget.attrs['class'] = 'form-control'
        for field, field_obj in cls.base_fields.items():
            field_obj.widget.attrs['class'] = 'form-control'
        return ModelForm.__new__(cls)

    class Meta:
        model = admin_class.model
        fields = '__all__'

    attrs = {
        'Meta': Meta,
        '__new__': __new__,
    }
    model_form = type('DynamicModelForm', (ModelForm,), attrs)
    return model_form
