# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import models
import urllib
from lxml import etree
import re
import requests
import time


# Create your views here.
def index(request):
    all_title = []
    list_time = str(time.time()).split('.')
    if int(list_time[1]) < 100:
        list_time[1] = '100'
    last_time = list_time[0] + list_time[1]
    # print last_time, type(last_time)
    uri = 'https://www.thepaper.cn/'
    params = 'load_index.jsp?&pageidx=2&lastTime=' + last_time
    url = uri + params
    # print url
    response = requests.get(url)
    # print response.status_code  # 响应的状态码
    # print response.content   # 返回字节信息
    # print response.text  # 返回文本内容

    html = etree.HTML(response.text)

    a_tesult = html.xpath('//h2/a')
    for a in a_tesult:
        mynews = {}
        a_text_title = a.xpath('./text()')
        if len(a_text_title):
            a_img = a.xpath('./../../div[1]/a/img/@src')
            # print '===>>>>>',a_img
            a_href = a.xpath('./@href')
            mynews['urls'] = uri + a_href[0]
            mynews['tt'] = a_text_title[0].encode('utf8')
            mynews['img'] = a_img[0]

            all_title.append(mynews)
        else:
            print u"没有爬到数据"

    return render(request, 'news/news.html', {'htmlcode': all_title})
    # return HttpResponse(all_title)


def details():
    pass
