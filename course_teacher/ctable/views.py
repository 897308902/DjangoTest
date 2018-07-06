# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from . import models
import string
from django.forms import ModelForm
from django.contrib.auth import authenticate, login
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
# @login_required
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


def tests(request, ids):
    return HttpResponse('sdfsfs:%s' % ids)


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # 跳转到成功页面
        return render(request,'index.html')
    else:
        # 返回一个非法登录的错误页面
        return render(request,'notfive.html')