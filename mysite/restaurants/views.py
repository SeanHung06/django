
# coding=Big5
from django.http import HttpResponse
from django.shortcuts import render
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
def menu(request):
    food1={'name':'番茄炒蛋','price':60,'comment':'好吃','is_spicy':False}
    food2={'name':'番茄蛋','price':70,'comment':'吃','is_spicy':False}
    food3={'name':'番茄蛋','price':70,'comment':'吃','is_spicy':False}
    food4={'name':'番茄蛋','price':70,'comment':'吃','is_spicy':False}
    food5={'name':'番茄蛋','price':70,'comment':'吃','is_spicy':False}
    foods=[food1,food2,food3,food4,food5]
    return render_to_response('menu.html',locals())
# Create your views here.
