# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 19:36
# @Author  : chengz
# @File    : myblog_urls.py
# @Software: PyCharm


from django.conf.urls import url
from . import views

urlpatterns = [

    # 用户博客页面(?P<name>.*?)
    url(r'^myblog/', views.userblog, name='mblog'),

    # 搜索我的博客
    url(r'^search/', views.mysearch, name='msearch'),

    # 按类别分类显示
    url(r'^(?P<name>.*?)/mark/(?P<tags>.*?)$', views.marks, name='mark'),

    # 编辑博客
    url(r'^modify$', views.edit_blog, name='modify'),

    # 新增博客
    url(r'^mdeditor/$', views.add_blog, name='mdeditor'),
    # 删除博客
    url(r'^del_blog$', views.del_blog, name='mdel'),



]
