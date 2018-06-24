# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Shopp(models.Model):
    name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=11)
    sex = models.IntegerField(null=True)
    pwd = models.CharField(max_length=20)
    email = models.CharField(max_length=20, null=True)
    ctime = models.CharField(max_length=30, null=True)
    utime = models.DateTimeField(max_length=30,null=True)

    class Meta:
        db_table = 'shopp'