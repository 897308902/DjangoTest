# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from shopapp.models import Shopp
import time


# Create your views here.

def index(request):
    return render_to_response('index.html')


def sales(request):
    return render_to_response('sales.html')


def regist(request):
    request.encoding = 'utf-8'

    if request.POST:
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        Shopp.objects.create(name=request.POST.get('usename'), phone=request.POST.get('phone'), pwd=request.POST['pwd1'],
                email=request.POST['email'], ctime=timestr, sex=request.POST.get('sex'))

    return render(request, 'regist.html')
