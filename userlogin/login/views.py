# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.
from userlogin import settings
from . import models
import hashlib


# def my_view(request):
#     if not request.user.is_authenticated():
#         return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def hash_code(s, salt='cz9025'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


# 首页
# def index(request):
#     blogs = models.Blogs.objects.all()
#
#     return render(request, 'login/index.html', {'blogs': blogs})

#搜索结果页面
def search(request, title):
    title =request.GET['title']
    titles = models.Blogs.objects.filter(title__contains=title)
    return render(request, 'login/index.html', {'blogs': titles})

# 博客详情页面
def blog_page(request, blog_id):
    blog = models.Blogs.objects.get(id=blog_id)
    return render(request, 'login/blog_page.html', {'blog': blog})


def login(request):
    # 如果登录了就进入首页
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    # 往session字典内写入用户状态和数据：
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index')
                else:
                    message = "密码不正确"
            except:
                message = "用户不存在!"
            return render(request, 'login/login.html', {'message': message})

    return render(request, 'login/login.html')


def register(request):
    # 如果是登录的就进入首页
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        email = request.POST.get('email', None)
        gender = request.POST.get('gender', None)
        if password1 != password2:
            message = "两次输入的密码不同！"
            return render(request, 'login/register.html', {'message': message})
        else:
            same_name = models.User.objects.filter(name=username)
            if same_name:
                message = '该用户名已存在，请重新输入用户名！'
                return render(request, 'login/register.html', {'message': message})
            same_email = models.User.objects.filter(email=email)
            if same_email:
                message = '该邮箱地址已被注册，请使用别的邮箱！'
                return render(request, 'login/register.html', {'message': message})

            user = models.User.objects.create(name=username, password=hash_code(password1), email=email, sex=gender)
            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return redirect('/index')

    return render(request, 'login/register.html')


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index')
    # 清空所有session
    request.session.flush()
    return redirect("/index/")


#我的博客
def userblog(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    # 获取当前登录的用户
    name = request.session.get('user_name')

    blogs= models.Blogs.objects.filter(uname = name)

    return render(request, 'login/userblog.html',{'blogs':blogs})



#编辑博客   添加博客
def edit_blog(request,blog_id):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    if str(blog_id) == '0':
        marks = models.Bmarks.objects.all()
        return render(request, 'login/edit_blog.html',{'marks':marks})
    else:

        blog = models.Blogs.objects.get(id=blog_id)
        marks = models.Bmarks.objects.all()
        return render(request, 'login/edit_blog.html', {'blog': blog, 'marks': marks})



def index(request):
    # 获取当前登录的用户
    name = request.session.get('user_name')
    if request.POST:
        blog_id=request.POST.get('blog_id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')


        if str(blog_id)=='0':
            models.Blogs.objects.create(title=title,content=content,marks_id=tags,uname_id=name)
            return redirect('/myblog/')
        else:
            article=models.Blogs.objects.get(id=blog_id)
            article.title=title
            article.content=content
            article.marks_id=tags
            article.save()
            return redirect('/myblog/')


    blogs=models.Blogs.objects.all()
    return render(request, 'login/index.html', {'blogs': blogs})


def marks(request,tags):
    blogs=models.Blogs.objects.filter(marks_id=tags)


    return render(request, 'login/marks.html', {'blogs': blogs})