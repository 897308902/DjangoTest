# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, render_to_response

from django.contrib.auth.models import User

# Create your views here.

# 自己的资料
from blog.models import Blogs


def centers(request):
    return render(request, 'center/center.html')


# 查看别人的资料
def usercenter(request, name):
    # 查用户的信息
    user = User.objects.get(username=name)

    # 查询出该用户的博客
    blogs = Blogs.objects.filter(uname=name).order_by('-utime')

    # 该用户博客标签
    marks = []
    for mark in blogs:
        if not mark.marks_id in marks:
            marks.append(mark.marks_id)

    return render(request, 'center/usercenter.html', {'blogs': blogs, 'user': user, 'marks': marks})
