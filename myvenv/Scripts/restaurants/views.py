# coding=Big5
from django.http import HttpResponse
from django.shortcuts import render
from django import template
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from restaurants.models import Restaurant,Food,Comment
from django.utils import timezone
def menu(request):
    path=request.path
    host=request.get_host()
    fullpath=request.get_full_path()
    secure=request.is_secure()
    if 'id' in request.GET and request.GET['id']!='':
        restaurant=Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html',locals())
    else:
        return HttpResponseRedirect('/restaurants_list/')

def list_restaurants(request):
    restaurants=Restaurant.objects.all()
    return render_to_response('restaurants_list.html',locals())
def comment(request,id):
    if id:
        r=Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect('/restaurants_list/')
    if request.POST:
        visitor=request.POST['visitor']
        content=request.POST['content']
        email=request.POST['email']
        date_time=timezone.localtime(timezone.now())
        Comment.objects.create(
                visitor=visitor,
                email=email,
                content=content,
                date_time=date_time,
                restaurant=r
        )
    return render_to_response('comments.html',RequestContext(request,locals()))











# Create your views here.