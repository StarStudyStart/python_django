import logging

from django.shortcuts import render

logging.basicConfig(level=logging.INFO)

# Create your views here.
from App.models import Carousel, MainNav, MainHot


def home(request):
    carousels = Carousel.objects.all()
    main_navs = MainNav.objects.all()
    main_hots = MainHot.objects.all()

    data = {
        'name': '首页',
        'carousels': carousels,
        'main_navs': main_navs,
        'main_hots': main_hots,
    }
    # logging.info('图片链接 %s', carousels.get(pk=1).img)

    return render(request, 'axf/main/home.html',context=data)


def market(request):
    return render(request, 'axf/main/market.html')


def mine(request):
    return render(request, 'axf/main/mine.html')


def cart(request):
    return render(request, 'axf/main/cart.html')