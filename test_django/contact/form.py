#!/usr/bin/env python
# coding:utf-8
"""
Name : form.py.py
Author  : yabinli
Time    : 2020/2/26 0026 12:00
"""

from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50, label='主题')
    email = forms.EmailField(required=False, label='邮箱地址')
    message = forms.CharField(widget=forms.Textarea, label='内容')

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.strip())
        print(num_words)
        if num_words < 4:
            raise forms.ValidationError('Not enough words!')
        return message
