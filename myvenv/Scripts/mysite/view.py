# coding=Big5
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
def here(request): 
    return HttpResponse('你好')
def math(request,a,b):
    a=int(a)
    b=int(b)
    s=a+b
    d=a-b
    p=a*b
    q=a/b
    return render_to_response('math.html',locals())
def menu(request):
    food1={'name':'番茄炒蛋','price':60,'comment':'好吃','is_spicy':False}
    food2={'name':'番茄蛋','price':70,'comment':'吃','is_spicy':False}
    food3={'name':'番茄蛋','price':70,'comment':'吃','is_spicy':False}
    food4={'name':'番茄蛋','price':70,'comment':'吃','is_spicy':False}
    food5={'name':'番茄蛋','price':70,'comment':'吃','is_spicy':False}
    foods=[food1,food2,food3,food4,food5]
    return render_to_response('menu.html',locals())
def welcome(request):
    if'user_name'in request.GET and request.GET['user_name'] !='':
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())
