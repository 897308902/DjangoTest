# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=11)
    sex=models.CharField(max_length=10)
    createtime = models.CharField(max_length=30)
