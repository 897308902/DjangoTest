# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    # 我的资料
    # url(r'^(?P<use>.*?)$', views.centers, name='mycenter'),
    url(r'^(?P<name>.*?)$', views.usercenter, name='usercenter'),

]
