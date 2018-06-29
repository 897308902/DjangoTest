# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Shopp(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    name = models.CharField(u"请输入名字", max_length=20, blank=False)
    phone = models.CharField(max_length=11, null=True)
    sex = models.CharField(max_length=2, null=True)
    pwd = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, null=True)
    ctime = models.DateTimeField(max_length=30, auto_now_add=True, null=False)  # 创建时间
    utime = models.DateTimeField(max_length=30, auto_now=True, null=False)  # 最后修改时间
