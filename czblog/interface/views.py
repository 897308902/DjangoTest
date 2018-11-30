# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import json
import requests


# Create your views here.


def index(request):
    return render(request, 'interface/interface.html')


def interface_get(request):
    if request.POST:
        urls = request.POST.get('urls')
        title = request.POST.get('title')
        print title
        # request.session['title'] = title

        response = requests.get(urls)
        resp = {'status': 10000, 'data': response.text}

        return HttpResponse(json.dumps(resp))
        # print title
    return render(request, 'interface/interface.html')
