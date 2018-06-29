# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BlogsPost


# Register your models here.
# class BlogsPostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'body', 'timestamp']
#

admin.site.register(BlogsPost)
