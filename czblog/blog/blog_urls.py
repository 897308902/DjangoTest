# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 18:26
# @Author  : chengz
# @File    : blog_urls.py
# @Software: PyCharm


from django.conf.urls import url
from . import views

urlpatterns = [

    # 首页
    url(r'^$', views.index),
    # 博客页面
    url(r'blog_page/(?P<blog_id>\d+)$', views.blog_page, name='blog_page'),
    # 搜索博客(?P<title>.*?)$
    url(r'^search/', views.search, name='indexsearch'),

    # 按类别分类显示
    url(r'^marks/(?P<tags>.*?)$', views.marks, name='marks'),
    # 评论
    # url(r'^comments', views.comments, name='comments'),
    # 错误页面
    url(r'^error', views.error, name='error'),

    # 点赞
    url(r'^(?P<blog_id>\d+)$', views.ulike, name='like'),
]
