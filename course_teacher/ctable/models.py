# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    period = models.IntegerField(db_index=True)
    description = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'course'


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.IntegerField(db_index=True)
    address = models.CharField(max_length=50, null=True)
    teacher = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='course', to_field='id' )

    class Meta:
        db_table = 'teacher'
