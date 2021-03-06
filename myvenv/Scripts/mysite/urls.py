"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from mysite.view import here,math,welcome
from restaurants.views import menu,list_restaurants,comment
admin.autodiscover() 
urlpatterns =[
    url(r'^admin/',include(admin.site.urls)),
    url(r'^here/$',here),
    url(r'^(\d{1,3})/math/(\d{1,3})/$',math), 
    url(r'^menu/$',menu),
    url(r'^welcome/$',welcome),
    url(r'^restaurants_list/$',list_restaurants),
    url(r'^comment/(\d{1,5})/$',comment),
]
