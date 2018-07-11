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

# 分类表
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


# 博客表
class Blogs(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    title = models.CharField(max_length=128, unique=True)
    # content = models.CharField(max_length=256)
    content = models.TextField()

    # 阅读量
    rcount = models.IntegerField(default=0)

    # 评论数
    coms = models.IntegerField(default=0)

    ctime = models.DateTimeField(max_length=30, auto_now_add=True, null=False)  # 创建时间
    utime = models.DateTimeField(max_length=30, auto_now=True, null=False)  # 最后修改时间

    marks = models.ForeignKey(Bmarks, null=True, on_delete=models.SET_DEFAULT, related_name='blog_marks',
                              to_field='tags', default="未分类")
    uname = models.ForeignKey(User, null=True, on_delete=models.SET_DEFAULT, related_name='auth_user',
                              to_field='username', default='匿名')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'user_blogs'
        unique_together = ('title',)
        verbose_name = "博客"
        verbose_name_plural = "博客"


# 评论表
class Comments(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    # 评论的内容
    comms = models.TextField(max_length=300)
    # 发表人  直接在views中获取当前登录的用户，保存起来
    uses = models.CharField(max_length=128, blank=False, default='匿名')
    # 博客相关的id
    cbid = models.IntegerField(null=True)
    cblog = models.CharField(max_length=128,null=True)
    ctime = models.DateTimeField(max_length=30, auto_now_add=True, null=True)  # 创建时间
    # 博客删除后，评论跟着删除
    # cblog = models.ForeignKey(Blogs, null=True, on_delete=models.SET_DEFAULT, related_name='user_blogs',
    #                           to_field='title', default="该博客已删除")

    # uses = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='auth_user', to_field='id')

    def __str__(self):
        return self.comms

    class Meta:
        db_table = 'use_comments'
