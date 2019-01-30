from django.urls import path, re_path
from django.conf.urls import url
from . import views

#添加命名空间
app_name = "learning_logs"

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    #path('topics/<int:topic_id>/', views.topic, name='topic')
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #用于添加新主题、新条目
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #编辑既有条目
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]