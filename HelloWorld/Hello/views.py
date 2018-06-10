# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response,HttpResponseRedirect
from django.http import HttpResponse


def index(request,id):
    return HttpResponse(u'<h1>dsfsafa</h1>===%s'%id)

def cheng(request):
    return render_to_response('first.html')
# Create your views here.


def two(request):
    
    return render_to_response('two.html')