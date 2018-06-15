# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 18:10
# @Author  : chengz
# @File    : search.py
# @Software: PyCharm

from django.http import HttpResponse
from django.shortcuts import render_to_response


# 表单
def search_form(request):
    return render_to_response('search_form.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = u'你搜索的内容为: ' + request.GET['q'] + request.GET['w']
    else:
        message = u'你提交了空表单'
    return HttpResponse(message)
