# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Blogs, Bmarks



@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'uname', 'marks', 'ctime')
    search_fields = ('title',)


@admin.register(Bmarks)
class BmarksAdmin(admin.ModelAdmin):
    list_display = ('tags',)
    search_fields = ('tags',)
