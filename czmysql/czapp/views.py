# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from czapp.models import Employee
import time


# def Add(request, name):
#     a = Employee.objects.create(name=name)
#     return HttpResponse("+++++".format(a.id))


# 接收请求数据
def regists(request):
    request.encoding = 'utf-8'
    t = {}
    if 'name' in request.GET:
        msg = request.GET['name'] + request.GET['pwd'] + request.GET['sex']
        if len(msg) < 1:
            msg = "没有输入内容"
        t['rlt'] = msg

        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        obj = Employee(name=request.GET['name'], phone=request.GET['pwd'], sex=request.GET['sex'], createtime=timestr)
        obj.save()

    # return HttpResponse(msg)  # 页面就只有文本内容了
    return render(request, 'regists.html', t)
