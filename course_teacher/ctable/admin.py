# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Course, Teacher


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'description')
    search_fields = ('title',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'address')
    search_fields = ('name',)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)


class MyAdminSite(admin.AdminSite):
    site_header = '欢迎登录管理网站'
    site_title = '管理网站'


admin_site = MyAdminSite()
admin_site.register(Course, CourseAdmin)
