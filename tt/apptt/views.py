# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import loader
from apptt.models import BlogsPost


def index(request):
    t = loader.get_template('index.html')
    context = {}
    context['hello'] = "hello django !!!"
    context['nick'] = u"昵称的"
    context['con'] = u"文本内容撒旦法发大沙发萨芬啊发生的发生发阿SA说发撒旦法阿斯顿撒发生发生的发生的打撒多少"
    context['time'] = "2018-06-11 15:31"
    return HttpResponse(t.render(context))


def today(request):
    t = loader.get_template('today.html')
    c = {'cz': 'qawsrftgyhuj'}
    return HttpResponse(t.render(c))


# def login_form(request):
#     return render_to_response('logins.html')
#

def login(request):
    request.encoding = 'utf-8'
    t = {}
    if 'name' in request.POST:
        msg = request.POST['name'] + request.POST['pwd']
        if len(msg) < 1:
            msg = "没有输入内容"
        t['rlt'] = msg

    # return HttpResponse(msg)  # 页面就只有文本内容了
    return render(request, 'logins.html', t)


def biao(request):
    t = {}
    request.encoding = 'utf-8'
    if 'a' in request.POST:
        msg = request.POST['a']
        t['a'] = msg

    return render(request, 'biaodan.html', t)


def kk(request):
    return render_to_response("two.html")


# 创建博客的
def blog_index(request):
    request.encoding = 'utf-8'
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request, 'blogs.html', {'blog_list': blog_list})  # 返回index.html页面
