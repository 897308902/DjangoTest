# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from django.shortcuts import render
import requests


def index(request):
    u"""先分开写着，到时再合并再一个方法中"""
    py_title = []
    rfs_title = []
    function_title = []
    interface_title = []
    jmeter_title = []

    # 左边是栏目，右边是详情
    # 点击左边的栏目发起一个get请求，带一个参数过去
    # 参考博雅  关于我们的页面
    def get_index(url):
        response = requests.get(url)
        if response.status_code == 200:
            # print response.encoding
            return response.text

    def get_py(res):
        res = res.result()
        html = etree.HTML(res)
        # 不包含特定元素的，这里排除为隐藏的元素
        result = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/h4/a')
        for li in result:
            mycsdn = {}
            title = li.xpath('./text()')
            if len(title):
                mycsdn['tt'] = title[1].strip()
                mycsdn['urls'] = li.xpath('./@href')[0]
                py_title.append(mycsdn)

    def get_rfs(res):
        res = res.result()
        html = etree.HTML(res)
        # 不包含特定元素的，这里排除为隐藏的元素
        result = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/h4/a')
        for li in result:
            mycsdn = {}
            title = li.xpath('./text()')
            if len(title):
                mycsdn['tt'] = title[1].strip()
                mycsdn['urls'] = li.xpath('./@href')[0]
                rfs_title.append(mycsdn)

    def get_jmeter(res):
        res = res.result()
        html = etree.HTML(res)
        # 不包含特定元素的，这里排除为隐藏的元素
        result = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/h4/a')
        for li in result:
            mycsdn = {}
            title = li.xpath('./text()')
            if len(title):
                mycsdn['tt'] = title[1].strip()
                mycsdn['urls'] = li.xpath('./@href')[0]
                jmeter_title.append(mycsdn)

    def get_function(res):
        res = res.result()
        html = etree.HTML(res)
        # 不包含特定元素的，这里排除为隐藏的元素
        result = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/h4/a')
        for li in result:
            mycsdn = {}
            title = li.xpath('./text()')
            if len(title):
                mycsdn['tt'] = title[1].strip()
                mycsdn['urls'] = li.xpath('./@href')[0]
                function_title.append(mycsdn)

    def get_interface(res):
        res = res.result()
        html = etree.HTML(res)
        # 不包含特定元素的，这里排除为隐藏的元素
        result = html.xpath('//*[@id="mainBox"]/main/div[2]/div[not(@style="display: none;")]/h4/a')
        for li in result:
            mycsdn = {}
            title = li.xpath('./text()')
            if len(title):
                mycsdn['tt'] = title[1].strip()
                mycsdn['urls'] = li.xpath('./@href')[0]
                interface_title.append(mycsdn)

    with ThreadPoolExecutor(10) as p:
        uri = "https://blog.csdn.net/cz9025/article/category/"
        # python
        p.submit(get_index, uri + '6810218').add_done_callback(get_py)
        # RF+SE
        p.submit(get_index, uri + '6810219').add_done_callback(get_rfs)
        # JMETER
        p.submit(get_index, uri + '6858016').add_done_callback(get_jmeter)
        # 接口测试
        p.submit(get_index, uri + '6966010').add_done_callback(get_interface)
        # 功能测试
        p.submit(get_index, uri + '6560600').add_done_callback(get_function)

    return render(request, 'csdn/csdn.html',
                  {'python': py_title, 'rfs': rfs_title, 'fun': function_title, 'intf': interface_title,
                   'jmeter': jmeter_title})
