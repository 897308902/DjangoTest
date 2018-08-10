# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 21:15
# @Author  : chengz
# @File    : resume_urls.py
# @Software: PyCharm


# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [

    # 首页
    url(r'^$', views.index, name='index'),

]
