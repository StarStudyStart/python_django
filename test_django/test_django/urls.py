"""test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from contact import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysite.urls')),
    path('advance_template/', include('advance_template.urls')),
    path('generic_view/', include('generic_view.urls')),
    path('not_html/', include('not_html.urls')),
    path('users/', include('users.urls')),
    path('contact/', contact_views.contact_us, name='contact'),
    path('contact/thanks/', contact_views.contact_thanks, name='contact'),
    path('contact/thanks/', contact_views.contact_thanks, name='contact'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns