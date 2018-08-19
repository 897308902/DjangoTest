# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, render_to_response

from django.contrib.auth.models import User

# Create your views here.

# 自己的资料
from blog.models import Blogs


# 查看资料  还没加分页功能
def usercenter(request, name):
    # 查用户的信息
    user = User.objects.get(username=name)

    # 查询出该用户的博客
    blogs = Blogs.objects.filter(uname=name).order_by('-utime')

    # 该用户博客标签
    mark = {}
    for mk in blogs:
        if not mark.has_key(mk.marks_id):
            k = Blogs.objects.filter(uname=name, marks=mk.marks_id)

            mark[mk.marks_id] = len(k)
            # print "biaoqian=======", mk.marks_id, len(k), mark

    # return  HttpResponse()
    return render(request, 'center/usercenter.html', {'blogs': blogs, 'user': user, 'mark': mark})
