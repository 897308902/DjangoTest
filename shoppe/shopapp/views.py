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
	lens=0
	if request.POST:
	 	lens = len(request.POST['usename'])
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        names = request.POST['usename'] if lens > 1 else "cz888"
        obj= Shopp(name=names,ctime=timestr,sex=request.POST['sex'])
        obj.save()


	return render_to_response('regist.html')