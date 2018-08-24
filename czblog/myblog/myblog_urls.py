# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 19:36
# @Author  : chengz
# @File    : myblog_urls.py
# @Software: PyCharm


from django.conf.urls import url
from . import views

urlpatterns = [

    # 用户博客页面(?P<name>.*?)
    url(r'^$', views.userblog, name='mblog'),

    # 搜索我的博客
    url(r'^search/', views.mysearch, name='msearch'),

    # 按类别分类显示
    url(r'^marks/(?P<tags>.*?)$', views.marks, name='mark'),

    # 编辑博客==添加   修改
    url(r'^(?P<name>.*?)/mdeditor/(?P<blog_id>\d+)$', views.edit_blog, name='medit'),
    # 删除博客
    url(r'^del_blog/(?P<blog_id>\d+)$', views.del_blog, name='mdel'),


    # 博客页面
    url(r'page/(?P<blog_id>\d+)$', views.blog_page, name='blog_page'),

]
