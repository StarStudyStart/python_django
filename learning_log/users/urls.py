from django.conf.urls import url
from django.contrib.auth.views import LoginView

app_name = "users"

urlpatterns = [
    # 登陆界面
    url(r'login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
]