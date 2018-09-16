# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request):
    # return HttpResponse('1')

    return render(request, 'myap/index.html',{'a':666})


def word(request):
    # 在这里进行数据库写操作
    return HttpResponse(1)


def te(request):
    return HttpResponse('cz')
