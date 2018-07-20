# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import models
from markdown import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# 主页搜索
def search(request):
    title = request.GET['title']
    titles = models.Blogs.objects.filter(title__contains=title).order_by('-rcount')
    return render(request, 'blog/index.html', {'blogs': titles})


# 我的博客搜索
def mysearch(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    name = request.user
    title = request.GET['title']
    titles = models.Blogs.objects.filter(uname=name, title__contains=title).order_by('-rcount')
    return render(request, 'blog/userblog.html', {'blogs': titles})


# 博客详情页面
def blog_page(request, blog_id):
    # if not request.user.is_authenticated:
    #     return redirect('/login/')

    blog = models.Blogs.objects.get(id=blog_id)
    # 评论
    if request.POST:
        # blogs = request.POST.get('blog_id')
        comms = request.POST.get('comment')
        uses = request.user
        models.Comments.objects.create(uses=uses, comms=comms, cbid=blog_id, cblog=blog.title)
        blog.coms = blog.coms + 1
        blog.save()
        return redirect('/blog/blog_page/%s' % blog_id)

    # 阅读量+1
    blog.rcount = blog.rcount + 1
    blog.save()

    # 评论显示,按博客的id查询
    comm = models.Comments.objects.filter(cbid=blog_id).order_by('-ctime')

    # 区分自己的和别人的博客uses
    # name = request.user
    # if name == blog.uname:
    #     return render(request, 'blog/blog_page.html', {'blog': blog, 'comm': comm})

    return render(request, 'blog/blog_page.html', {'blog': blog, 'comm': comm})


# 博客详情页面，评论翻页   没有做了
def compage(request, blog_id):
    cpage = models.Comments.objects.filter(cbid=blog_id).order_by('-ctime')

    # 生成paginator对象,定义每页显示10条记录
    paginator = Paginator(cpage, 10)
    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)

    try:
        cpage = paginator.page(currentPage)  # 获取当前页码的记录
    except PageNotAnInteger:
        cpage = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        cpage = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, '/blog/blog_page/%s' % (blog_id), locals())


# 我的博客
def userblog(request):
    # 如果没登录就需先登录
    if not request.user.is_authenticated:
        return redirect('/login/')
    # 获取登录的用户名
    name = request.user
    contents = None

    if request.POST:
        blog_id = request.POST.get('blog_id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')

        # 非空判断title   content

        # 添加博客
        if str(blog_id) == '0':
            if not title:
                marks = models.Bmarks.objects.all()
                return render(request, 'blog/edit_blog.html', {'logs': '6666666', 'marks': marks})
            # print 'add==========',markdown(content)
            models.Blogs.objects.create(title=title, content=markdown(content), marks_id=tags, uname_id=name)
            return redirect('/myblog/')
        # 修改博客
        else:
            article = models.Blogs.objects.get(id=blog_id)
            article.title = title
            #
            article.content = markdown(content)
            article.marks_id = tags
            article.save()
            # print 'edit==============',article.content
            return redirect('/myblog/')

    blogs = models.Blogs.objects.filter(uname=name).order_by('-rcount')
    print '=========', len(blogs)

    b = models.Blogs.objects.get(id=6)
    # print 'out==============', b.content

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

    return render(request, 'blog/userblog.html', locals())


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


# 删除博客   删除有问题，删除后，地址错误，
def del_blog(request, blog_id):
    num = models.Blogs.objects.get(id=blog_id).delete()
    if num:
        return redirect('/myblog/')
    blogs = models.Blogs.objects.all().order_by('-rcount')
    return render(request, 'blog/userblog.html', {'blogs': blogs})


# 首页
def index(request):
    blogs = models.Blogs.objects.all().order_by('-rcount')  # [0:10]
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
    return render(request, 'blog/index.html', locals())  # {'blogs': blogs}


# 按标签
def marks(request, tags):
    blogs = models.Blogs.objects.filter(marks_id=tags).order_by('-rcount')
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

    return render(request, 'blog/marks.html', locals())


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
            info = "输入的旧密码不正确"
            return render(request, "blog/set_pwd.html", {"logs": info})
    return render(request, "blog/set_pwd.html")


# 登录
def uselogin(request):
    if request.method == 'GET':
        # 记住来源的url,如果没有则设置为首页('/')
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # 重定向到来源的url
            return HttpResponseRedirect(request.session['login_from'])
            # return redirect('/blog/')
        else:
            return render(request, 'blog/login.html', {'logs': '账号或密码错误'})

    return render(request, 'blog/login.html', {'logs': ' '})


# 注册
def reg(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # password2 = request.POST.get("password2")
        email = request.POST.get("email")
        # first_name=request.POST.get("first_name")
        # last_name = request.POST.get("last_name")
        # if password1 != password2:
        #     return render(request, "blog/register.html", {'logs': '两次密码出入不一致'})
        name = User.objects.filter(username=username)
        # 如果用户存在，则name=1,不存在则name=0
        if name:
            return render(request, "blog/register.html", {'message': '用户已存在%s' % len(name)})
        # else:
        # return render(request, "regist.html", {'logs': '用户bu存在%s' % len(name)})
        # 得到用户输入的用户名和密码创建一个新用户
        User.objects.create_user(username=username, password=password, email=email)

        # 注册成功后自动登录
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/blog/")
    return render(request, "blog/register.html")


# 注销
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/blog/")
