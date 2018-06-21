# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render_to_response,HttpResponseRedirect
from django.http import HttpResponse
import datetime
from django.template import loader
# Create your views here.


class Person(object):
	"""docstring for Person"""
	def __init__(self, name,age,sex):
		
		self.name = name
		self.age=age
		self.sex=sex
		
	def say(self):
		return "my name is "+self.name

def test(request):
	t=loader.get_template('test.html')
	# user={"name":"tom","age":27,"sex":"man"}

	per=Person("chengz",27,"mans")
	book=["python","c","java"]
	dic={"a":1,"b":2,"c":3}
	c={"title":datetime.datetime.now(),"name":"Django","user":per,"book":book,"dic":dic}

	return HttpResponse(t.render(c))  