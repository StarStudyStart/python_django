from django.urls import path

from App import views

app_name = 'axf'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('mine/', views.mine, name='mine'),
    path('cart/', views.cart, name='cart'),
]