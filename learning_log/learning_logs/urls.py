from django.urls import path
from django.conf.urls import url
from . import views

#添加命名空间
app_name = "learning_logs"

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    #path('topics/<int:topic_id>/', views.topic, name='topic')
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]