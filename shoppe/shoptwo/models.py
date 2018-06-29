# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

KIND_CHOICES = (
    ('python', 'python'),
    ('java', 'java'),
    ('script', 'script'),
    ('android', 'android'),
    ('else', 'else'),
)


class Moment(models.Model):
    content = models.CharField(max_length=200, blank=False)
    user_name = models.CharField(u"请输入名字", max_length=20, default='匿名', blank=False)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])

    class Meta:
        db_table = 'Moment'
