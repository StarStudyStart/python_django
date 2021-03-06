from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
import markdown

from comments.forms import CommentForm


# Create your views here.
# 博客文章列表
def index(request):
    '''return render(request,'blog/index.html',context = {
        'title':'我的博客首页',
        'welcome':'欢迎访问我的博客首页'})'''
    #post_list = Post.objects.all().order_by('-create_time') # '-'表示逆序
    post_list = Post.objects.all()
    return render(request,'blog/index.html',context = {'post_list':post_list})
    
#跳转文章详情
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'comment_list': comment_list,
               'form': form
               }
    return render(request,'blog/detail.html', context=context)
    
#归档详情列表
def archives(request,year,month):
    post_list = Post.objects.filter(create_time__year = year,
                                    create_time__month = month) #.order_by('-create_time')
    return render(request,'blog/index.html',context = {'post_list':post_list})
    
#分类详情列表
def category(request,pk):
    cate = get_object_or_404(Category,pk = pk)
    post_list = Post.objects.filter(category = cate) #.order_by('-create_time')
    return render(request,'blog/index.html',context = {'post_list':post_list})
    
    

