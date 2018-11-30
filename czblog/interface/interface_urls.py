# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 18:26
# @Author  : chengz
# @File    : blog_urls.py
# @Software: PyCharm


from django.conf.urls import url
from . import views

urlpatterns = [

    # 接口首页
    url(r'^$', views.index, name='index'),
    url(r'^post$', views.interface_get, name='get'),

]
