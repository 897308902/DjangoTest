# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 单独的一个用户信息表
# class UserInfo(models.Model):
#     nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
#     birthday = models.DateField(null=True, blank=True, verbose_name='生日')
#     gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female',
#                               verbose_name='性别')
#     address = models.CharField(max_length=100, default='', verbose_name='地址')
#     mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
#     head_img = models.CharField(max_length=255, verbose_name='用户头像')
#     uname = models.ForeignKey(to=User, null=True, on_delete=models.SET_DEFAULT,
#                               to_field='username', default='匿名', verbose_name="用户名")
#
#     class Meta:
#         db_table = 'user_info'
#         verbose_name = '用户信息'
#         verbose_name_plural = verbose_name
