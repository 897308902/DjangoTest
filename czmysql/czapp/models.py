# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Employee(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30, null=False, default='cz666')
    phone = models.CharField(max_length=20, default="88888888888")
    sex = models.CharField(max_length=10, default='3')
    email = models.EmailField(null=True, default="a@b.com", max_length=20)
    createtimes = models.CharField(max_length=30, null=True)
    # uptime = models.DateTimeField(auto_now=True, null=True)
  #   class Meta:
		# db_table='Employee'



# manage.py inspectdb   先创建表，然后反向生成class