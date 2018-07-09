# -*- coding: utf-8 -*-
"""course_teacher URL Configuration

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
from ctable import views

from django.contrib.auth import urls as auth_urls

from ctable.admin import admin_site

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin_site.urls),
    url(r'^index', views.index, name='index'),
    url(r'^addCourse', views.addCourse, name='addCourse'),
    url(r'^addTeacher', views.addTeacher, name='addTeacher'),
    url(r'^dels', views.dels, name='delCourse'),
    # url(r'^accounts/', include(auth_urls, namespace='accounts')),

    url(r'^tests', views.tests, name='tests'),


    # 登录
    url(r'^login', views.uselogin, name='uselogin'),
    # 注册
    url(r'^reg', views.reg, name='regist'),

    # 注销
    url(r'^logout', views.log_out, name='log_out'),
    # 修改密码
    url(r'^setpwd', views.set_pwd, name='set_pwd'),



]

# 这个name的名字可以随意取，但在其他地方使用时就要用这个
