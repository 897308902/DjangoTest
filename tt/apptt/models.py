# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length=150)  # 博客标题
    body = models.TextField()  # 博客正文
    timestamp = models.DateTimeField(auto_now_add=True)  # 创建时间
