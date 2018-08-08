# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [

    # 首页
    url(r'^$', views.index, name='index'),

]
