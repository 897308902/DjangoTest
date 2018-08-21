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
from blog.models import Bmarks, Blogs,Comments


def userblog(request):
    # return HttpResponse(8888)
    # 如果没登录就需先登录
    if not request.user.is_authenticated:
        return redirect('/login/')
    # 获取登录的用户名
    name = request.user
    print '======', type(request.user.username)
    contents = None
    # 添加   修改   博客的请求
    if request.POST:
        blog_id = request.POST.get('blog_id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')

        # 非空判断title   content

        # 添加博客
        if str(blog_id) == '0':
            if not title:
                marks = Bmarks.objects.all()
                return render(request, 'myblog/edit_blog.html', {'logs': '6666666', 'marks': marks})
            # print 'add==========',markdown(content)
            Blogs.objects.create(title=title, content=markdown(content), marks_id=tags, uname_id=name)
            # 地址是什么就写什么
            return redirect('/user/')
        # 修改博客
        else:
            article = Blogs.objects.get(id=blog_id)
            article.title = title
            #
            article.content = markdown(content)
            article.marks_id = tags
            article.save()
            # print 'edit==============',article.content
            return redirect('/user/')
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


# 编辑博客   添加博客
def edit_blog(request,name,blog_id):
    # return HttpResponse('edit_blog')
    if not request.user.is_authenticated:
        return redirect('/login/')

    if str(blog_id) == '0':
        marks = Bmarks.objects.all()
        return render(request, 'myblog/edit_blog.html', {'marks': marks})
    else:

        blog = Blogs.objects.get(id=blog_id)
        marks = Bmarks.objects.all()
        return render(request, 'myblog/edit_blog.html', {'blog': blog, 'marks': marks})


# 删除博客   删除有问题，删除后，地址错误，
def del_blog(request, blog_id):
    # return HttpResponse('del_blog')
    num = Blogs.objects.get(id=blog_id).delete()
    if num:
        return redirect('/user/')
    blogs = Blogs.objects.all().order_by('-rcount')
    return render(request, 'myblog/userblog.html', {'blogs': blogs})

# 按标签
def marks(request, tags):
    # return HttpResponse('marks')
    if not request.user.is_authenticated:
        return redirect('/login/')
    name=request.user
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


# 博客详情页面
def blog_page(request, blog_id):
    # return HttpResponse('11blog_page')
    # if not request.user.is_authenticated:
    #     return redirect('/login/')
    # blog=None
    try:
        blog = Blogs.objects.get(id=blog_id)
        # 阅读量+1
        blog.rcount = blog.rcount + 1
        blog.save()
    except:
        return redirect('/user/error.html')

    # 评论
    if request.POST:
        # blogs = request.POST.get('blog_id')
        comms = request.POST.get('comment')
        uses = request.user
        Comments.objects.create(uses=uses, comms=comms, cbid=blog_id, cblog=blog.title)
        blog.coms = blog.coms + 1
        blog.save()
        return redirect('/user/blog_page/%s' % blog_id)

    # 评论显示,按博客的id查询
    comm = Comments.objects.filter(cbid=blog_id).order_by('-ctime')
    return render(request, 'myblog/blog_page.html', {'blog': blog, 'comm': comm})

