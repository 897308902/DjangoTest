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


def biao(request):
    t = {}
    request.encoding = 'utf-8'
    if 'a' in request.POST:
        msg = request.POST['a']
        t['a'] = msg

    return render(request, 'biaodan.html', t)


# 创建博客的
# 博客列表
def blog_index(request):
    request.encoding = 'utf-8'
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    # blog_list = BlogsPost.objects.filter(id__in = [1,2,3])  # 获取所有数据
    return render(request, 'blogs.html', {'blog_list': blog_list})  # 返回index.html页面


# 添加博客
def adds(request):
    request.encoding = 'utf-8'
    if request.POST:
        tit = request.POST['tit']
        con = request.POST['con']
        BlogsPost.objects.create(title=tit, body=con)
    # 添加完成回到主页
    # blog_list = BlogsPost.objects.all()
    # return render(request, 'blogs.html', {'blog_list': blog_list})
    return render(request, 'adds.html')


# 博客详情页面
def blog_page(request, article_id):
    article = BlogsPost.objects.get(id=article_id)
    return render(request, "page.html", {'article': article})


# 修改博客
def upblog(request, article_id):
    article = BlogsPost.objects.get(id=article_id)
    return render(request, "upblog.html", {'article': article})


def edit(request):
    if request.POST:
        newtitle = request.POST.get('tit')
        newcon = request.POST.get('con')
        nowid = request.POST.get('id')
        if str(nowid) == '0':

            BlogsPost.objects.create(title=newtitle, body=newcon)
            blog_list = BlogsPost.objects.all()
            return render(request, 'blogs.html', {'blog_list': blog_list})
        else:
            BlogsPost.objects.filter(id=nowid).update(title=newtitle, body=newcon)
            article = BlogsPost.objects.get(id=nowid)
            return render(request, "page.html", {'article': article})
