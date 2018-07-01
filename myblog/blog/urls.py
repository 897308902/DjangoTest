from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^index', views.index),
    url(r'^page/(?P<article_id>\d+)$',views.page,name='page'),
    url(r'^edit/(?P<article_id>\d+)$',views.edit, name='edit'),
    url(r'^index',views.action,name='action'),



]
