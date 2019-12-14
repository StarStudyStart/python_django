from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = "users"

urlpatterns = [
    # 登陆界面
    path('login/', LoginView.as_view(template_name='../templates/users/login.html'), name='login'),
    # 登出界面
    path('logout/', views.logout_view, name='logout'),
    # 注册页面
    path('register/', views.register, name='register'),
]