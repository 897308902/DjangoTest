# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
import models


# 首页
def index(request):
    old_url = request.get_full_path()
    # arg_urls = request.get_full_path()
    print "===index=get_full_path===", old_url
    blogs = models.Blogs.objects.all().order_by('-ctime')  # [0:10]
    # print blogs
    # 生成paginator对象,定义每页显示10条记录
    paginator = Paginator(blogs, 10)
    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)
    try:
        blogs = paginator.page(currentPage)  # 获取当前页码的记录
    except PageNotAnInteger:
        blogs = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    # locals()函数会以字典类型返回当前位置的全部局部变量。
    return render(request, 'blog/index.html', locals())


# 主页搜索  增加翻页        搜索的结果翻页会报错
def search(request):
    title = request.GET.get('title')
    s = request.build_absolute_uri()
    print (s)
    arg_urls = request.path[0:-1] + "?title=" + title
    print (arg_urls)

    # 增加翻页
    blogs = models.Blogs.objects.filter(title__contains=title).order_by('-ctime')

    # 生成paginator对象,定义每页显示10条记录
    paginator = Paginator(blogs, 10)
    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)

    try:
        blogs = paginator.page(currentPage)  # 获取当前页码的记录
    except PageNotAnInteger:
        blogs = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return render(request, 'blog/index.html', locals())


# 错误页面
def error(request):
    return render(request, 'error.html')


# 博客详情页面
def blog_page(request, blog_id):
    # return HttpResponse(6)
    if not request.user.is_authenticated:
        return redirect('/login/')
    # blog=None
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/blog')
    try:
        blog = models.Blogs.objects.get(id=blog_id)
        # 阅读量+1
        blog.rcount = blog.rcount + 1
        blog.save()
    except:
        return render(request, 'error.html')

    # 评论
    if request.POST:
        blog = models.Blogs.objects.get(id=blog_id)
        # blogs = request.POST.get('blog_id')
        comms = request.POST.get('comment')
        uses = request.user
        models.Comments.objects.create(uses=uses, comms=comms, cbid=blog_id, cblog=blog.title)
        #
        count = models.Comments.objects.filter(cbid=blog_id)
        # print u"某个博客的评论数据===", len(count)
        blog.coms = len(count)
        blog.save()
        # print "=================提交评论成功================="
        # 这个只能用重定向，不然刷新页面还会提交
        print 'pinglun===url=>>>>', request.path
        # return redirect(request.path)
        return redirect('/blog/%s' % blog_id)
        # return redirect('/blog/')

    # 评论显示,按博客的id查询
    comm = models.Comments.objects.filter(cbid=blog_id).order_by('-ctime')

    # 区分自己的和别人的博客uses
    # name = request.user
    # if name == blog.uname:
    #     return render(request, 'blog/blog_page.html', {'blog': blog, 'comm': comm})

    return render(request, 'blog_page.html', {'blog': blog, 'comm': comm})


# 点赞功能
def ulike(request, blog_id):
    # if request.GET:
    # 判断当前用户是否点赞
    if not request.user.is_authenticated:
        return redirect('/login/')

    name = request.user
    islike = models.Likes.objects.filter(like_user=name, like_id=blog_id)
    print ("dianzan::::::::", islike)
    # 没有点赞时
    if not islike:
        blike = models.Blogs.objects.get(id=blog_id)
        blike.like = blike.like + 1

        blike.save()
        # 保存谁点赞的
        models.Likes.objects.create(like_user=name, like_title=blike.title, like_id=blog_id)
        print ("点赞成功:::::", blike.like)
        return HttpResponse(1)
    else:
        return HttpResponse(2)


# 删除自己的评论   查询语句需再优化
def del_comms(request, blog_id):
    delId = request.GET.get("id")
    print ("delid===", delId)
    models.Comments.objects.filter(id=delId).delete()
    #
    blog = models.Blogs.objects.get(id=blog_id)
    count = models.Comments.objects.filter(cbid=blog_id)
    print ("某个博客的评论数据===", len(count))
    blog.coms = len(count)
    blog.save()

    return HttpResponse(1)


# 博客详情页面，评论翻页       没有做了
def compage(request, blog_id):
    cpage = models.Comments.objects.filter(cbid=blog_id).order_by('-ctime')

    # 生成paginator对象,定义每页显示10条记录
    paginator = Paginator(cpage, 10)
    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)

    try:
        cpage = paginator.page(currentPage)  # 获取当前页码的记录
    except PageNotAnInteger:
        cpage = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        cpage = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, '/blog/%s' % blog_id, locals())


# 按标签
def marks(request, tags):
    blogs = models.Blogs.objects.filter(marks_id=tags).order_by('-ctime')
    # 生成paginator对象,定义每页显示10条记录
    paginator = Paginator(blogs, 10)
    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)

    try:
        blogs = paginator.page(currentPage)  # 获取当前页码的记录
    except PageNotAnInteger:
        blogs = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'blog/marks.html', locals())
