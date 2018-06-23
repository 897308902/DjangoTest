# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse
from czapp.models import Employee
import time


def index(request):
    request.encoding = 'utf-8'
    return render_to_response('base.html')


# 接收请求数据
def regists(request):
    request.encoding = 'utf-8'
    t = {}
    if request.GET:
        lens = len(request.GET['usename'])
        msg = str(lens) + request.GET['usename'] + request.GET['phone'] + request.GET['sex'] + request.GET['email']

        # if len(msg) < 1:
        #     msg = "没有输入内容"
        t['rlt'] = msg

        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        # 也可以用此种方式创建
        # obj = Employee(name=request.GET['name'],phone=request.GET['pwd'],sex=request.GET['sex'],createtimes=timestr)
        # obj.save()

        # 增加数据
        names = request.GET['usename'] if lens > 1 else "cz888"
        Employee.objects.create(name=names, phone=request.GET['phone'], sex=request.GET['sex'],
                                createtimes=timestr, email=request.GET['email'])

    return render_to_response('regists.html', t)


def dels(request):
    request.encoding = "utf-8"
    t = loader.get_template('deletes.html')
    c = {}
    if request.GET:
        names = request.GET['names']
        num = Employee.objects.filter(name=names).count()
        Employee.objects.filter(name=names).delete()  # 这个计数不正确，需找个方法

        if num > 0:
            c['shan'] = u'你删除了所有name=' + names + u"；共删除" + str(num) + u"条数据"
        else:
            c['shan'] = u'要删除的名字不存在'

    return HttpResponse(t.render(c))


def updates(request):
    request.encoding = 'utf-8'
    n = {}
    if request.GET:

        id = request.GET["ids"]  # 待修改的条件
        uname = request.GET["upname"]  # 待修改的名字

        nname = Employee.objects.filter(id=id).update(name=uname)
        if nname == 1:
            names = Employee.objects.get(name=uname)  # 按修改后的名字查询

            n['uname'] = u"修改成功,新名字为：" + names.name
        else:
            n['uname'] = u"修改失败"
    return render(request, "updates.html", n)


def search(request):
    request.encoding = 'utf-8'
    t = loader.get_template('search.html')
    c = {}
    if request.GET:
        searchname = request.GET['queryname']
        names = Employee.objects.filter(name=searchname)
        c = {'con': names}
    return HttpResponse(t.render(c))

def test(request):
    t=loader.get_template('test.html')

    emp=Employee.objects.all()
    c={"data":emp}

    return HttpResponse(t.render(c))