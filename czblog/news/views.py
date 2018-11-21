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


# Create your views here.
def index(request):
    response = requests.get('https://www.thepaper.cn/channel_25950')
    html = etree.HTML(response.text)
    all_title = []
    #

    #
    artical = html.xpath('//div[@id="masonryContent"]/div')
    # print artical
    print len(artical)

    print '============>>>>'
    for tit in artical:
        mynews = {}

        title = tit.xpath('./h2/a/text()')
        href = tit.xpath('./h2/a/@href')
        if title:
            uri = 'https://www.thepaper.cn/'

            # print title[0].encode('utf8'), 'https://www.thepaper.cn/' + href[0]
            # if href:

            # 新闻详情
            response = requests.get(uri + href[0])
            html = etree.HTML(response.text)
            news_title = html.xpath('//h1[@class="news_title"]/text()')
            if news_title:
                mynews['urls'] = uri + href[0]
                # print href[0]
                # print news_title[0].encode('utf8')
                mynews['tt'] = news_title[0]

            img = html.xpath('//div[@class="news_txt"]/div[1]/img/@src')
            # if img:
            #     mynews['img'] = img[0]
            news_content = html.xpath('//div[@class="news_txt"]/text()')
            # for cons in news_content:
            #     print cons

            all_title.append(mynews)
        else:
            print u"没有爬到数据"

    return render(request, 'news/news.html', {'htmlcode': all_title})
    # return HttpResponse(all_title)


def details():
    pass
