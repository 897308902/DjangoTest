# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, render_to_response


# Create your views here.


def centers(request):
    return render(request, 'center/center.html')
