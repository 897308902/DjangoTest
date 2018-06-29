# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import MentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def welcome(request):
    return HttpResponse('welcome')


def moments_input(request):
    if request.POST:
        form = MentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("shoptwo.views.welcome"))
    else:
        form = MentForm()
        return render(request, 'moments_input.html', {'form': form})




