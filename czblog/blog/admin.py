# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Blogs, Bmarks, Comments, Likes


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rcount', 'coms', 'like', 'uname', 'marks', 'ctime')
    search_fields = ('title',)
    date_hierarchy = 'ctime'
    # ordering = ('ctime',)
    # fields = ('title','coms')   # 在后台编辑博客时，只能修改这些字段


@admin.register(Bmarks)
class BmarksAdmin(admin.ModelAdmin):
    list_display = ('tags',)
    search_fields = ('tags',)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comms', 'cblog', 'uses')
    search_fields = ('comms',)


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('like_user', 'like_title')
    search_fields = ('like_title',)
