# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader
from shopapp.models import Shopp
import time
# Create your views here.

def index(request):

	return render_to_response('index.html')

def sales(request):
	return render_to_response('sales.html')

def regist(request):
	request.encoding = 'utf-8'
	timestr='00000000'
	if request.POST:
		timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

        obj= Shopp(name=request.POST.get('usename'), phone=request.POST.get('phone'), 
        	ctime=timestr,sex=request.POST.get('sex'))
        obj.save()


	return render_to_response('regist.html')