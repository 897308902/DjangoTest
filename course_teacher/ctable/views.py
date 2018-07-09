# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from . import models
import string
from django.forms import ModelForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect


# 添加数据  分开添加，课程为课程，老师为老师

def addCourse(request):
    if request.POST:
        title = request.POST.get('title')
        period = request.POST.get('period')
        description = request.POST.get('description')

        try:
            # 判断数据库中是否存在这个课程，，如果存在则tit为Course object对象
            tit = models.Course.objects.get(title=title)
            # 如果存在，则处理
            if tit:
                print tit
                pass
            # else:
            #     models.Course.objects.create(title=title, period=period, description=description)
        except:

            ok = models.Course.objects.create(title=title, period=period, description=description)
            if ok:
                print "添加成功,课程id=", ok.id

                return HttpResponseRedirect(reverse('index'))
            else:
                print 666666666666, ok

    return render(request, 'addCourse.html')


def addTeacher(request):
    cour = models.Course.objects.all()
    t = {'course': cour}
    if request.POST:
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        # 获取课程的ID
        teacher_id = request.POST.get('course_id')

        ok = models.Teacher.objects.create(name=name, gender=gender, address=address, teacher_id=teacher_id)
        if ok:
            print "添加成功,id=", ok.id

            return HttpResponseRedirect(reverse('index'))
        else:
            print 666666666666, ok

    return render(request, 'addTeacher.html', t)


# 删除数据

def dels(request):
    if request.POST:
        titles = request.POST.get('title')
        cour = models.Course.objects.get(title=titles)
        cour.delete()
        if cour:
            print "删除成功,", cour

            return HttpResponseRedirect(reverse('index'))
        else:
            print "删除失败,", cour

    return render(request, 'dels.html')


# @cache_page(60 * 15)  # 秒数，这里指缓存 15 分钟，不直接写900是为了提高可读性

def index(request):
    # if not request.user.is_authenticated:
    #     return redirect('dels.html')
    cour = models.Course.objects.all()
    c = []
    tea = models.Course
    for i in cour:
        # form = MomentForm()
        try:
            # 如果某个课程没有教师的话，则为空
            tea = models.Teacher.objects.get(teacher_id=i.id)
            if not tea:
                tea.name = ""
                break
        except:
            tea.name = ""

        c.append(tea.name)

    t = {'course': cour, 'teacher': c}
    return render(request, 'index.html', t)


# @login_required
def tests(request):
    # 如果登录了就退出
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)

    name = request.user.username
    pwd = request.user.password
    return HttpResponse('6666666666%s,%s' % (name, pwd))


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
            return render(request, "set_pwd.html", {"logs": info})
    return render(request, "set_pwd.html")


# 登录
def uselogin(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'logs': '账号或密码错误'})

    return render(request, 'login.html', {'logs': ' '})


# 注册
def reg(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        name = User.objects.filter(username=username)
        # 如果用户存在，则name=1,不存在则name=0
        if name:
            return render(request, "regist.html", {'logs': '用户已存在%s' % len(name)})
        # else:
            # return render(request, "regist.html", {'logs': '用户bu存在%s' % len(name)})
        # 得到用户输入的用户名和密码创建一个新用户
        User.objects.create_user(username=username, password=password)  # User是以个对象
        # s = "恭喜你注册成功，现在可以登录了"
        return redirect("/index/")
    return render(request, "regist.html")


# 注销
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/login/")
