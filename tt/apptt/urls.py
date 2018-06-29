# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 14:49
# @Author  : chengz
# @File    : urls.py
# @Software: PyCharm


from django.conf.urls import url
from django.contrib import admin
from apptt import views


# from . import login

urlpatterns = [

    url(r'^blog', views.blog_index),
    url(r'^page/(?P<article_id>\d+)$', views.blog_page, name='blog_page'),
    url(r'^adds', views.adds),

]
