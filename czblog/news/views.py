# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import models
import urllib


# Create your views here.
def index(request):
    page = urllib.urlopen('https://news.baidu.com/guonei')  # 打开网页
    htmlcode = page.read()  # 读取页面源码
    # return render(request, 'news/news.html', {'htmlcode': htmlcode})
    return HttpResponse(htmlcode)
