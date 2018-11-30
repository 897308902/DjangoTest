# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import models
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import re
import requests
import time


# Create your views here.
def qindex121(request):
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


def index(request):
    sina_title = []
    paper_title = []
    baidu_title = []
    car_title = []

    def get_index(url):
        u"""通用请求"""
        respose = requests.get(url)
        if respose.status_code == 200:
            print u"编码方式==>>>", respose.encoding
            return respose.text

    def sina_news(res):
        u"""新浪"""
        res = res.result()  # 进程执行完毕后，得到1个对象
        html = etree.HTML(res)
        # 最新新闻
        result = html.xpath('//div[@class="zgjq"]//ul//a')
        print len(result)
        for li in result:
            mynews = {}
            titlt = li.xpath('./text()')
            if len(titlt):
                # print titlt[0].encode('ISO-8859-1'),
                # print li.xpath('./@href')
                mynews['tt'] = titlt[0].encode('ISO-8859-1')
                mynews['urls'] = li.xpath('./@href')[0]
                sina_title.append(mynews)

    def paper_news(res):
        u"""澎湃"""
        res = res.result()
        html = etree.HTML(res)
        uri = 'https://www.thepaper.cn/'
        a_tesult = html.xpath('//h2/a')
        for a in a_tesult:
            mynews = {}
            a_img = a.xpath('./../../div[1]/a/img/@src')
            atext = a.xpath('./text()')
            ahref = a.xpath('./@href')
            # print atext[0], uri + ahref[0], a_img
            mynews['tt'] = atext[0]
            mynews['urls'] = uri + ahref[0]
            mynews['img'] = a_img[0]
            paper_title.append(mynews)

    def baidu_news(res):
        u"""百度"""
        res = res.result()
        html = etree.HTML(res)
        result = html.xpath('//ul[contains(@class,"ulist")]//a')
        # print len(result)
        # global title
        for li in result:
            mynews = {}
            # print li.xpath('./text()')[0],
            # print li.xpath('./@href')
            mynews['tt'] = li.xpath('./text()')[0]
            mynews['urls'] = li.xpath('./@href')[0]
            baidu_title.append(mynews)

    def car_news(res):
        u"""环球汽车"""
        res = res.result()
        html = etree.HTML(res)

        result = html.xpath('//ul[@class="iconBoxT14"]//a')
        # print len(result)
        for a in result:
            mynews = {}
            a_text = a.xpath('./text()')[0].encode('ISO-8859-1')
            if len(a_text):
                mynews['tt'] = a_text
                # print a_text
                mynews['urls'] = a.xpath('./@href')[0]
                car_title.append(mynews)

    with ThreadPoolExecutor(max_workers=4) as p:
        # 新浪军情
        p.submit(get_index, 'https://mil.news.sina.com.cn/').add_done_callback(sina_news)
        # 国内新闻
        p.submit(get_index, 'https://news.baidu.com/guonei').add_done_callback(baidu_news)
        # 环球汽车
        p.submit(get_index, 'http://auto.huanqiu.com/').add_done_callback(car_news)
        list_time = str(time.time()).split('.')
        if int(list_time[1]) < 100:
            list_time[1] = '100'
        last_time = list_time[0] + list_time[1]
        # 时事
        p.submit(get_index,
                 'https://www.thepaper.cn/load_index.jsp?&pageidx=2&lastTime=' + last_time).add_done_callback(
            paper_news)
    return render(request, 'news/news.html',
                  {'sina_title': sina_title, 'paper_title': paper_title, 'baidu_title': baidu_title,
                   'car_title': car_title})
