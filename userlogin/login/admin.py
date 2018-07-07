# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import User, Blogs, Bmarks


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'c_time')
    search_fields = ('name',)


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'uname', 'marks', 'ctime')
    search_fields = ('title',)


@admin.register(Bmarks)
class BmarksAdmin(admin.ModelAdmin):
    list_display = ('tags',)
    search_fields = ('tags',)
