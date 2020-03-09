import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse

from mysite.models import Book


def get_current(request,year):
    """获取当前时间"""
    # print(type(year))
    # return HttpResponse("type of year"+year)
    now = datetime.datetime.now()
    name = 'yabin'
    return render(request, "mysite/index.html", locals())


def display_meta(request):
    """显示请求头信息"""
    values = request.META.items()
    return render(request, "mysite/display_meta.html", {'values':values})


def search_results(request, query=''):
    """表单请求"""
    books = Book.objects.filter(title__icontains=query)
    return render(request, "mysite/search_results.html", {'query':query,'books':books})


def search(request):
    """转化链接"""
    errors = []
    if request.method == 'POST':
        query = request.POST['q']
        if not query:
            errors.append("query为空")
        elif len(query) > 20:
            errors.append("超过20字符")
        else:
            return HttpResponseRedirect(reverse('mysite:search_results', args=(query,)))
    return render(request, 'mysite/search_form.html', {'errors': errors})