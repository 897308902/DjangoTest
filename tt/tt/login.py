# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 9:09
# @Author  : chengz
# @File    : login.py
# @Software: PyCharm

from django.http import HttpResponse
from django.shortcuts import render_to_response, render


def login_form(request):
    return render_to_response('logins.html')


def login(request):
    request.encoding = 'utf-8'
    t = {}
    if request.POST:
        msg = "----------" + request.POST['name'] + request.POST['pwd']
        if len(msg) < 2:
            msg = ""
        t['rlt'] = msg

    # return HttpResponse(msg)  # 页面就只有文本内容了
    return render(request, 'logins.html', t)
