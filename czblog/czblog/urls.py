# -*- coding: utf-8 -*-
"""czblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 用户博客页面
    url(r'^myblog', views.userblog, name='userblog'),
    # 搜索我的博客
    url(r'^myblog/mysearch/', views.mysearch, name='mysearch'),

    # 编辑博客==添加   修改
    url(r'^edit_blog/(?P<blog_id>\d+)$', views.edit_blog, name='edit_blog'),
    # 删除博客
    url(r'^del_blog/(?P<blog_id>\d+)$', views.del_blog, name='del_blog'),

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

    # 个人资料相关的
    url(r'^center/', include('center.center_urls', namespace='center')),
    # 博客相关的
    url(r'^blog/', include('blog.blog_urls', namespace='blog')),
    # 新闻模块
    url(r'^news/', include('news.news_urls', namespace='news')),

]
