# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Moment

class MomentAdmin(admin.ModelAdmin):
	list_display=('title','content','kind','ctime')
	list_filter=('ctime',)
		


admin.site.register(Moment,MomentAdmin)