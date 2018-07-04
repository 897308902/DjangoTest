# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse

from . import models
import string


# 添加数据  分开添加，课程为课程，老师为老师

def addCourse(request):
    if request.POST:
        title = request.POST.get('title')
        period = request.POST.get('period')
        description = request.POST.get('description')
        try:
            tit = models.Course.objects.get(title=title)
            if tit:
                pass
            # else:
            #     models.Course.objects.create(title=title, period=period, description=description)
        except:
            models.Course.objects.create(title=title, period=period, description=description)

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

        models.Teacher.objects.create(name=name, gender=gender, address=address, teacher_id=teacher_id)

    return render(request, 'addTeacher.html', t)


# 删除数据

def dels(request):
    if request.POST:
        titles = request.POST.get('title')
        cour = models.Course.objects.get(title=titles)
        cour.delete()

    return render(request, 'dels.html')


def index(request):
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
