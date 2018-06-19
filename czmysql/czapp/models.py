# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=30, null=False)
    phone = models.IntegerField(max_length=11, null=False)
    sex = models.CharField(max_length=10, null=False)
    email = models.EmailField(null=True, default="a@b.com", max_length=20)
    createtime = models.CharField(max_length=30, null=False)
    uptime = models.DateTimeField(auto_now=True, null=False)
