# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# unique唯一db_index索引
# 课程不能重名 老师也不能重名

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("课程名称", max_length=50, null=False, unique=True)  # 课程
    period = models.IntegerField("课程学时", db_index=True)  # 课时
    description = models.CharField("课程描述", max_length=200, null=True)  # 课程描述

    class Meta:
        unique_together = ('title',)
        db_table = 'course'

    def __unicode__(self):
        return self.title


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("教师名字", max_length=50, unique=True, null=False, db_index=True)  # 名字
    gender = models.IntegerField("教师性别")  # 性别
    address = models.CharField("教师住址", max_length=50, null=True)  # 住址
    teacher = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL, related_name='course', to_field='id')

    class Meta:
        db_table = 'teacher'

#
# CASCADE:这就是默认的选项，级联删除，你无需显性指定它。
# PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
# SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
# SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。


