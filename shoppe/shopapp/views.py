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
        Shopp.objects.create(name=request.POST.get('usename'), phone=request.POST.get('phone'), ctime=timestr,
                             pwd=request.POST['pwd1'], sex=request.POST.get('sex'), email=request.POST['email'])

    return render(request, 'regist.html')


def login(request):
    request.encoding = 'utf-8'
    t = {}
    if request.POST:
        phone = request.POST.get('phone')
        pwd = request.POST.get('pwd')

        # 这样可以多条件查询
        names = Shopp.objects.filter(phone=phone, pwd=pwd).count()

        if names == 1:
            t['hh'] = u"登录成功"
        elif names == 0:
            t['hh'] = u"没有该用户"
        else:
            t['hh'] = names

    return render(request, 'login.html', t)
