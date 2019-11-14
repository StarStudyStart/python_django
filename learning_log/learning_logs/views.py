from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
import markdown


def index(request):
    return render(request, "learning_logs/index.html")


@login_required
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {'topics': topics}
    return render(request, "learning_logs/topics.html", context)


@login_required
def topic(request, topic_id):
    """显示单个主题的所有项目"""
    topic = Topic.objects.get(pk=topic_id)
    # 确认请求是否来自当前用户
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    for entry in entries:
        entry.text = markdown.markdown(entry.text,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
    context = {
        'topic': topic,
        'entries': entries
    }
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # post提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """为特定主题添加新条目"""
    
    topic = Topic.objects.get(pk=topic_id)
    
    if request.method != 'POST':
        # 未提交数据，创建一个新的表单
        form = EntryForm()
    else:
        # post提交数据,对数据进行处理。存储到数据库中
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=(topic.id,)))
                
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(pk=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # 未提交数据，使用当前条目填充数据
        form = EntryForm(instance=entry)
    else:
        # post提交数据，对原有条目实例进行替换
        form = EntryForm(instance=entry, data=request.POST)  #不要忘记，表单提交数据存放于request.POST中
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                args=(topic.id, )))
                
    context = {'form':form, 'topic':topic, 'entry':entry}
    return render(request, 'learning_logs/edit_entry.html', context)