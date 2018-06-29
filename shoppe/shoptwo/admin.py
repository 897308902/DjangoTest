# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Moment
# 添加需要管理的模型类
admin.site.register(Moment)
