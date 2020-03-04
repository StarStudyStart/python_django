#!/usr/bin/env python
# coding:utf-8
"""
Name : views.py
Author  : yabinli
Time    : 2020/2/26 0026 10:49
Desc:
"""

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404

from contact.form import ContactForm


def contact_us(request, ):
    errors = []
    if request.method == 'POST':
        # if not request.POST.get('subject', ''):
        #     errors.append('Enter a subject.')
        # if not request.POST.get('message', ''):
        #     errors.append('Enter a message.')
        # if request.POST.get('email') and '@' not in request.POST['email']:
        #     errors.append('Enter a valid e‐mail address.')
        # if not errors:
        #     print('test')
        #     send_mail(
        #         request.POST['subject'],
        #         request.POST['message'],
        #         '18792146966@163.com',
        #         ['1403913161@qq.com',],
        #     )
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                '18792146966@163.com',
                ['1403913161@qq.com',],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
           form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact/contact_form.html', {'form': form})
    # return render(request, 'contact/contact_form.html', {
    #             'errors': errors,
    #             'subject': request.POST.get('subject', ''),
    #             'message': request.POST.get('message', ''),
    #             'email': request.POST.get('email', ''),
    #         })


def contact_thanks(request):
    return HttpResponse("<P>发送成功！</P>")