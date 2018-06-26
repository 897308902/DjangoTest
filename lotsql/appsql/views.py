# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from appsql.models import Student, Teacher


# Create your views here.

def student_list(request):
    t = loader.get_template('student.html')
    # studentList=Student.objects.all().order_by('-age')
    teacher = Teacher.objects.get(id=1)
    studentList = teacher.student_teacher.all()  # 默认 student_set，但不要定义外键名

    c = {"studentList": studentList}
    return HttpResponse(t.render(c))
