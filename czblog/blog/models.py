# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
#
# class User(models.Model):
#     gender = (
#         ('male', "男"),
#         ('female', "女"),
#     )
#     id = models.AutoField(max_length=10, primary_key=True)
#     name = models.CharField(max_length=128, unique=True)
#     password = models.CharField(max_length=256)
#
#     email = models.EmailField(unique=True)
#     sex = models.CharField(max_length=32, choices=gender, default="男")
#     c_time = models.DateTimeField(auto_now_add=True, null=False)
#     u_time = models.DateTimeField(auto_now=True, null=False)  # 最后修改时间
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'login_user'
#         ordering = ["-c_time"]
#         verbose_name = "用户"
#         verbose_name_plural = "用户"
#         unique_together = ('name',)


class Bmarks(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    tags = models.CharField(max_length=128, unique=True, null=False)

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'blog_marks'
        unique_together = ('tags',)
        verbose_name = "分类"
        verbose_name_plural = "分类"


class Blogs(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    title = models.CharField(max_length=128, unique=True)
    # content = models.CharField(max_length=256)
    content = models.TextField()

    ctime = models.DateTimeField(max_length=30, auto_now_add=True, null=False)  # 创建时间
    utime = models.DateTimeField(max_length=30, auto_now=True, null=False)  # 最后修改时间

    marks = models.ForeignKey(Bmarks, null=True, on_delete=models.SET_NULL, related_name='blog_marks', to_field='tags',
                              default="未分类")
    uname = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='auth_user', to_field='username',
                              default='匿名')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'user_blogs'
        unique_together = ('title',)
        verbose_name = "博客"
        verbose_name_plural = "博客"
