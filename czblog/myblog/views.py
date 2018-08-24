# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from . import models
from markdown import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from blog.models import Blogs
# Create your views here.

# 我的博客
from blog.models import Bmarks, Blogs, Comments


def userblog(request):
    # return HttpResponse(8888)
    # 如果没登录就需先登录
    if not request.user.is_authenticated:
        return redirect('/login/')
    # 获取登录的用户名
    name = request.user
    print '===userblog===', request.user.username, type(request.user.username)

    # 增加翻页
    blogs = Blogs.objects.filter(uname=name).order_by('-rcount')

    # 生成paginator对象,定义每页显示10条记录
    paginator = Paginator(blogs, 10)
    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)

    try:
        blogs = paginator.page(currentPage)  # 获取当前页码的记录
    except PageNotAnInteger:
        blogs = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return render(request, 'myblog/userblog.html', locals())


# 我的博客搜索
def mysearch(request):
    # return HttpResponse('11111111111111111')
    if not request.user.is_authenticated:
        return redirect('/login/')
    name = request.user
    title = request.GET.get('title')
    # 增加翻页
    blogs = Blogs.objects.filter(uname=name, title__contains=title).order_by('-rcount')
    # 生成paginator对象,定义每页显示10条记录
    paginator = Paginator(blogs, 10)
    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)

    try:
        blogs = paginator.page(currentPage)  # 获取当前页码的记录
    except PageNotAnInteger:
        blogs = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return render(request, 'myblog/userblog.html', locals())


# 编辑博客
def edit_blog(request, blog_id):
    # return HttpResponse('edit_blog')
    if not request.user.is_authenticated:
        return redirect('/login/')
    # name = request.user

    # 该博客的原标题
    old_title = None
    try:
        # 判断一种被删除的情况，再编辑的同时被删除了
        blog = Blogs.objects.get(id=blog_id)
        old_title = blog.title
    except:
        # 如果这个博客被删除了，就返回一个错误页面
        return redirect('/blog/error.html')

    if request.POST:
        # 如果标题还是为空的话，证明该博客已经被删除了
        if not old_title:
            return redirect('/blog/error.html')
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')
        # 如果博客存在，则判断
        try:
            tit = Blogs.objects.get(title=title)
            # 跟原始标题相同之外的就都提示已经存在
            if not tit.title == old_title:
                return HttpResponse('已经存在该名称')
        except:
            pass

        article = Blogs.objects.get(id=blog_id)
        article.title = title
        #
        article.content = markdown(content)
        article.marks_id = tags
        article.save()

        # 添加完成重定向到我的博客
        return redirect('/myblog/')

    blog = Blogs.objects.get(id=blog_id)
    marks = Bmarks.objects.all()
    return render(request, 'myblog/edit_blog.html', {'blog': blog, 'marks': marks})


# 增加博客
def add_blog(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    name = request.user
    if request.POST:
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')

        # 非空判断title   content
        if not title:
            marks = Bmarks.objects.all()
            return render(request, 'myblog/add_blog.html', {'logs': '6666666', 'marks': marks})

        # 如果博客存在，则判断
        try:

            tit = Blogs.objects.get(title=title)
            if tit:
                return HttpResponse('已经存在该名称')
        except:
            pass

        Blogs.objects.create(title=title, content=markdown(content), marks_id=tags, uname_id=name)
        # 添加完成重定向到我的博客
        return redirect('/myblog/')

    marks = Bmarks.objects.all()
    return render(request, 'myblog/add_blog.html', {'marks': marks})


# 删除博客   删除有问题，删除后，地址错误，
def del_blog(request, blog_id):
    # return HttpResponse('del_blog')
    num = Blogs.objects.get(id=blog_id).delete()
    if num:
        return redirect('/myblog/')
    blogs = Blogs.objects.all().order_by('-rcount')
    return render(request, 'myblog/userblog.html', {'blogs': blogs})


# 按标签
def marks(request, tags):
    # return HttpResponse('marks')
    if not request.user.is_authenticated:
        return redirect('/login/')
    name = request.user
    blogs = Blogs.objects.filter(uname=name, marks_id=tags).order_by('-rcount')
    # 生成paginator对象,定义每页显示10条记录
    paginator = Paginator(blogs, 10)
    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)

    try:
        blogs = paginator.page(currentPage)  # 获取当前页码的记录
    except PageNotAnInteger:
        blogs = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return render(request, 'myblog/marks.html', locals())
