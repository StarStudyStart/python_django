from django.urls import path

from App import views

app_name = 'axf'
urlpatterns = {
    path('home/', views.home, name='home'),
}