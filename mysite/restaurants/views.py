
# coding=Big5
from django.http import HttpResponse
from django.shortcuts import render
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
def menu(request):
    food1={'name':'�f�X���J','price':60,'comment':'�n�Y','is_spicy':False}
    food2={'name':'�f�X�J','price':70,'comment':'�Y','is_spicy':False}
    food3={'name':'�f�X�J','price':70,'comment':'�Y','is_spicy':False}
    food4={'name':'�f�X�J','price':70,'comment':'�Y','is_spicy':False}
    food5={'name':'�f�X�J','price':70,'comment':'�Y','is_spicy':False}
    foods=[food1,food2,food3,food4,food5]
    return render_to_response('menu.html',locals())
# Create your views here.
