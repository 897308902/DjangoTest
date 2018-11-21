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
    # mynews = {}

    #
    artical = html.xpath('//div[@id="masonryContent"]/div')
    # print artical
    print len(artical)

    print '============>>>>'
    for tit in artical:

        title = tit.xpath('./h2/a/text()')
        href = tit.xpath('./h2/a/@href')
        if title:

            # print title[0].encode('utf8'), 'https://www.thepaper.cn/' + href[0]
            # 新闻详情
            response = requests.get('https://www.thepaper.cn/' + href[0])
            html = etree.HTML(response.text)
            news_title = html.xpath('//h1[@class="news_title"]/text()')[0]
            all_title.append(news_title)
            # print news_title, '\n'

            img = html.xpath('//div[@class="news_txt"]/div[1]/img/@src')
            # if img:
                # all_title
                # mynews['img'] = img[0]
            #     print img[0]
            news_content = html.xpath('//div[@class="news_txt"]/text()')
            # for cons in news_content:
            #     print cons
            # print '\n'
            # mynews['tt'] = news_title

            # all_title.append(mynews)
            print all_title
        else:
            print u"没有爬到数据，别看了"

    return render(request, 'news/news.html', {'htmlcode': all_title})
    # return HttpResponse(all_title)


def crawl():
    data = {}
    # 澎湃  时事
    response = requests.get('https://www.thepaper.cn/channel_25950')
    html = etree.HTML(response.text)
    #
    artical = html.xpath('//div[@id="masonryContent"]/div')
    # print artical
    print len(artical)

    print '============>>>>'
    for tit in artical:

        title = tit.xpath('./h2/a/text()')
        href = tit.xpath('./h2/a/@href')
        if title:
            # print title[0].encode('utf8'), 'https://www.thepaper.cn/' + href[0]
            # 新闻详情
            response = requests.get('https://www.thepaper.cn/' + href[0])
            html = etree.HTML(response.text)
            news_title = html.xpath('//h1[@class="news_title"]/text()')[0].encode('utf-8')
            print news_title, '\n'
            img = html.xpath('//div[@class="news_txt"]/div[1]/img/@src')
            if img:
                print img[0]
            news_content = html.xpath('//div[@class="news_txt"]/text()')
            for cons in news_content:
                print cons
            print '\n'
        else:
            print u"没有爬到数据，别看了"
