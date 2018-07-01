# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import Moment

# 博客主页
# def index(request):
	# article=Moment.objects.all()

	# return render(request,'blog/index.html',{'article':article})

# 博客详情页面
def page(request,article_id):
	article=Moment.objects.get(id=article_id)
	return render(request,'blog/page.html',{'article':article})

# 编辑页面
def edit(request,article_id):
	if str(article_id)=='0':
		# article=Moment.objects.get(id=article_id)
		return render(request,'blog/edit.html')
	else:
		article=Moment.objects.get(id=article_id)
		return render(request,'blog/edit.html',{'article':article})

# 编辑页面提交后回到主页
def action(request):
	if request.POST:
		article_id=request.POST.get('article_id')
		title=request.POST.get('title')
		content=request.POST.get('content')
		kind= request.POST.get('kind')

		# Moment.objects.create(title=title,content=content)

		#如果是0的话就新建博客
		if str(article_id)=='0':
			Moment.objects.create(title=title,content=content,kind=kind)

			# article=Moment.objects.all()

			# return render(request,'blog/index.html',{'article':article})
		else:
			article=Moment.objects.get(id=article_id)
			article.title=title
			article.content=content
			article.kind=kind
			article.save()

	# 不管是新建还是编辑，提交后都进入首页
	article=Moment.objects.all()
	return render(request,'blog/index.html',{'article':article})
	# return HttpResponseRedirect(request.session['index'])
