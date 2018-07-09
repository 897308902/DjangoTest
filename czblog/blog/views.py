# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from czblog import settings
from . import models
import hashlib


def hash_code(s, salt='cz9025'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


# 搜索结果页面
def search(request, title):
    title = request.GET['title']
    titles = models.Blogs.objects.filter(title__contains=title)
    return render(request, 'blog/index.html', {'blogs': titles})


# 博客详情页面
def blog_page(request, blog_id):
    blog = models.Blogs.objects.get(id=blog_id)
    return render(request, 'blog/blog_page.html', {'blog': blog})


# 我的博客
def userblog(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    # 获取当前登录的用户
    name = request.user

    blogs = models.Blogs.objects.filter(uname=name)

    return render(request, 'blog/userblog.html', {'blogs': blogs})


# 编辑博客   添加博客
def edit_blog(request, blog_id):
    if not request.user.is_authenticated:
        return redirect('/login/')

    if str(blog_id) == '0':
        marks = models.Bmarks.objects.all()
        return render(request, 'blog/edit_blog.html', {'marks': marks})
    else:

        blog = models.Blogs.objects.get(id=blog_id)
        marks = models.Bmarks.objects.all()
        return render(request, 'blog/edit_blog.html', {'blog': blog, 'marks': marks})


def index(request):
    # 获取当前登录的用户
    if request.user.is_authenticated:
        name = request.user

    if request.POST:
        blog_id = request.POST.get('blog_id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')

        if str(blog_id) == '0':
            models.Blogs.objects.create(title=title, content=content, marks_id=tags, uname_id=name)
            return redirect('/myblog/')
        else:
            article = models.Blogs.objects.get(id=blog_id)
            article.title = title
            article.content = content
            article.marks_id = tags
            article.save()
            return redirect('/myblog/')

    blogs = models.Blogs.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})


def marks(request, tags):
    blogs = models.Blogs.objects.filter(marks_id=tags)

    return render(request, 'blog/marks.html', {'blogs': blogs})


# 使用user模块注册登录


# 修改密码
def set_pwd(request):
    if request.method == "POST":
        oldpassword = request.POST.get("oldpassword")
        newpassword = request.POST.get("newpassword")
        # 得到当前登录的用户，判断旧密码是不是和当前的密码一样
        username = request.user  # 打印的是当前登录的用户名
        user = User.objects.get(username=username)  # 查看用户
        ret = user.check_password(oldpassword)  # 检查密码是否正确
        if ret:
            user.set_password(newpassword)  # 如果正确就给设置一个新密码
            user.save()  # 保存
            return redirect("/login/")
        else:
            info = "输入密码有误"
            return render(request, "blog/set_pwd.html", {"logs": info})
    return render(request, "blog/set_pwd.html")


# 登录
def uselogin(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/index/')
        else:
            return render(request, 'blog/login.html', {'logs': '账号或密码错误'})

    return render(request, 'blog/login.html', {'logs': ' '})


# 注册
def reg(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(request, "blog/register.html", {'logs': '两次密码出入不一致'})
        name = User.objects.filter(username=username)
        # 如果用户存在，则name=1,不存在则name=0
        if name:
            return render(request, "blog/register.html", {'logs': '用户已存在%s' % len(name)})
        # else:
        # return render(request, "regist.html", {'logs': '用户bu存在%s' % len(name)})
        # 得到用户输入的用户名和密码创建一个新用户
        User.objects.create_user(username=username, password=password1)  # User是以个对象

        # 注册成功后自动登录
        user = authenticate(username=username, password=password1)
        if user:
            login(request, user)
            return redirect("/index/")
    return render(request, "blog/register.html")


# 注销
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/index/")
