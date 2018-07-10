# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 18:26
# @Author  : chengz
# @File    : blog_urls.py
# @Software: PyCharm



from django.conf.urls import url, include
from django.contrib import admin

from blog import views

urlpatterns = [


    # 博客页面
    url(r'blog_page/(?P<blog_id>\d+)$', views.blog_page, name='blog_page'),
    # 搜索博客(?P<title>.*?)$
    # url(r'^index/search/', views.search, name='indexsearch'),
    # 搜索我的博客
    url(r'^myblog/mysearch/', views.mysearch, name='mysearch'),

    # 用户博客页面
    url(r'^myblog', views.userblog, name='userblog'),
    # 编辑博客==添加   修改
    url(r'^edit_blog/(?P<blog_id>\d+)$', views.edit_blog, name='edit_blog'),
    # 删除博客
    url(r'^del_blog/(?P<blog_id>\d+)$', views.del_blog, name='del_blog'),
    # 首页
    url(r'^index', views.index, name='action'),
    # 按类别分类显示

    url(r'^marks/(?P<tags>.*?)$', views.marks, name='marks'),

    # 登录
    url(r'^login', views.uselogin, name='uselogin'),
    # 注册
    url(r'^register', views.reg, name='register'),

    # 退出登录
    url(r'^logout', views.log_out, name='log_out'),
    # 修改密码
    url(r'^setpwd', views.set_pwd, name='set_pwd'),

]
