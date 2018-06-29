# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 17:06
# @Author  : chengz
# @File    : forms.py
# @Software: PyCharm


from django.forms import ModelForm
from .models import Moment


class MentForm(ModelForm):
    class Meta:
        model = Moment
        fields = '__all__'
