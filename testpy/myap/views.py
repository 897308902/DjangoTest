# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request):
    return render(request,'myap/index.html')


def word(request):
    li = [1, 2, 3]
    return render(request, 'index.html', {'lis': li})
