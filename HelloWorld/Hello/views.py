# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response,HttpResponseRedirect
from django.http import HttpResponse


# def index(request,id):
#     return HttpResponse(u'<h1>dsfsafa</h1>===%s'%id)

def cheng(request):
    return render_to_response('first.html')
# Create your views here.


def about(request):
    
    return render_to_response('about.html')

def game(request):
    
    return render_to_response('game.html')

def index(request):
    
    return render_to_response('index.html')


def joins(request):
    
    return render_to_response('joins.html')

def news(request):
    
    return render_to_response('news.html')

def recruitment(request):
    
    return render_to_response('recruitment.html')


def services(request):
    
    return render_to_response('services.html')








