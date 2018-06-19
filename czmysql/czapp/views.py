# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse
from czapp import models
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
        msg = request.GET['name'] + request.GET['pwd'] + request.GET['sex']+request.GET['email']
        if len(msg) < 1:
            msg = "没有输入内容"
        t['rlt'] = msg

        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        # obj = Employee(name=request.GET['name'], phone=request.GET['pwd'], sex=request.GET['sex'], createtime=timestr)
        # obj.save()

        # 增加数据
        Employee.objects.create(name=request.GET['name'], phone=request.GET['pwd'], sex=request.GET['sex'],
                                createtime=timestr, email=request.GET['email'])

    # return HttpResponse(msg)  # 页面就只有文本内容了
    return render(request, 'regists.html', t)


def dels(request):
    Employee.objects.filter(id=25).delete()

    return HttpResponse("delete id=25")


def updates(request):
    Employee.objects.filter(id='27').update(name='qinj')
    return HttpResponse("updates id=27")


def search(request):
    t = loader.get_template('search.html')
    name = Employee.objects.all().values("name")
    c = {'con': name}
    return HttpResponse(t.render(c))
