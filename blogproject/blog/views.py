from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.
def index(request):
    '''return render(request,'blog/index.html',context = {
        'title':'我的博客首页',
        'welcome':'欢迎访问我的博客首页'})'''
    post_list = Post.objects.all().order_by('-create_time') # '-'表示逆序
    return render(request,'blog/index.html',context = {'post_list':post_list})
    
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/detail.html',context = {'post':post})
