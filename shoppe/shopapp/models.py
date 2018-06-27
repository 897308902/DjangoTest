# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Shopp(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20, null=True, default='c666')
    phone = models.CharField(max_length=11, null=True)
    sex = models.CharField(max_length=2, null=True, default='3')
    pwd = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, null=True, default="a@b.com", )
    ctime = models.CharField(max_length=30, null=True)
