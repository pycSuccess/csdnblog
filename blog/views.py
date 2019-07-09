from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.urls import reverse
from django.db.models import Count
import json
# Create your views here.


from blog.models import Article
from blog.models import UserInfo
from blog.models import Category
from blog.models import Tag


def index(request):
    article_list = Article.objects.all()
    return render(request, 'index.html', {'article_list': article_list})


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = auth.authenticate(username=user, password=pwd)
        if user:
            auth.login(request, user)
            url = reverse('index')
            return redirect(url)
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    url = reverse('index')
    return redirect(url)


def home_site(request, username):
    user = UserInfo.objects.filter(username=username).first()
    if not user:
        return render(request, 'not_found.html')
    article_list = Article.objects.filter(user__username=username)
    blog = user.blog
    cate_list = Category.objects.filter(blog=blog).annotate(c=Count('article__nid')).values('title', 'c')
    tag_list = Tag.objects.filter(blog=blog).annotate(c=Count('article__nid')).values('title', 'c')
    dict = {
        "blog": blog,
        "article_list": article_list,
        "category_count": cate_list,
        "tag_count": tag_list,
    }
    print(cate_list, type(cate_list))
    return render(request, 'home_work.html', dict)


# 查询当前站点每一个分类的名称以及对应的文章数
# 查询当前站点每一个标签的名称以及对应的文章数
def home_work(request):
    # articles = Article.objects.all().annotate(c=Count('nid')).values('category__title', 'c').distinct()
    # articles = Category.objects.all().annotate(c=Count('article__nid')).values('title', 'c')
    # print(articles)
    # articles = Tag.objects.all().annotate(c=Count('article__nid')).values('title', 'c')
    # print(articles)
    # test_date = Article.objects.filter(comment_count=0).extra(select={'y_m_date': 'create_time' > '2017-09-05'})
    # print(test_date)
    date_list = Article.objects.all().extra(select={"y_m_date": "date_format('%%Y/%%m',create_time)"}).values(
        "y_m_date")
    print(date_list[0].get('y_m_date'))
    return HttpResponse('ok')
