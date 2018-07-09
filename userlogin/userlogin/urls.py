"""userlogin URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import authenticate, login
from django.contrib.auth import urls as auth_urls
from login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/', include('users.urls')),
    url(r'^accounts/', include(auth_urls, namespace='accounts')),
    # url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),

    url(r'blog_page/(?P<blog_id>\d+)$', views.blog_page, name='blog_page'),

    url(r'^search/(?P<title>.*?)$', views.search, name='search'),
    url(r'^myblog', views.userblog, name='userblog'),

    url(r'^edit_blog/(?P<blog_id>\d+)$',views.edit_blog,name='edit_blog'),
    url(r'^index',views.index,name='action'),
    url(r'^marks/(?P<tags>.*?)$',views.marks,name='marks'),

    url(r'^auth_view',views.auth_view),


]
