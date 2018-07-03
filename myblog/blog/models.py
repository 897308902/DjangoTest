# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
KIND_CHOICES = (
    ('python', 'python'),
    ('java', 'java'),
    ('script', 'script'),
    ('android', 'android'),
    ('else', 'else'),
)
# article  member

class Moment(models.Model):
    title = models.CharField(u"文章标题", max_length=20, blank=False)
    content = models.CharField("文章内容", max_length=200, blank=False)
    kind = models.CharField("文章类型", max_length=20, choices=KIND_CHOICES)
    ctime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Moment'

    def __unicode__(self):
        return self.title
