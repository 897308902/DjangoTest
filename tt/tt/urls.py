"""tt URL Configuration

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
from apptt import views
from tapptwo import views as two
from . import search, search2

# from . import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', views.index),
    url(r'^search-form', search.search_form),
    url(r'^search', search.search),
    url(r'^search-post', search2.search_post),
    url(r'^today', views.today),
    url(r'^biao', views.biao),

    url(r'^blogs/$', include('apptt.urls')),
    url(r'^blogs', views.blog_index, name='blogs'),
    url(r'^page/(?P<article_id>\d+)$', views.blog_page, name='blog_page'),
    url(r'^upblog/(?P<article_id>\d+)$', views.upblog, name='upblog'),
    url(r'^edit', views.edit),
    url(r'^adds/$', views.adds),







    url(r'^atwo', two.tapptwo,name='tapptwo'),

]
