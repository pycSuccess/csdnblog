from django.shortcuts import render, HttpResponse, redirect
import json
from django.contrib import auth
from django.urls import reverse
from django.views import View
from django.http import JsonResponse
from rest_framework import serializers
from news import models

# Create your views here.


def index(request):
    return HttpResponse('通过ajax进行登录操作完成')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(username, pwd)
        user = auth.authenticate(username=username, password=pwd)
        ret = {'status': 0, 'url': ''}
        if user:
            auth.login(request, user)
            ret['status'] = 1
            ret['url'] = reverse('index')
            print(ret)
            return HttpResponse(json.dumps(ret))
    return render(request, 'login.html')


class Logout(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


def insert_into(request):
    # models.Tag.objects.create(name='python')
    # models.Tag.objects.create(name='django')
    # models.Tag.objects.create(name='vue')
    # models.School.objects.create(name='北京校区')
    # models.School.objects.create(name='上海校区')
    # models.School.objects.create(name='深圳校区')
    # models.Article.objects.create(title='python三年用不上', type=1,school_id=1)
    # models.Article.objects.create(title='你不可能知道Vue有多简单', type=2,school_id=2)
    # models.Article.objects.create(title='Mysql一点都不难', type=2,school_id=3)
    tag = models.Tag.objects.filter(id=1).first()
    article = models.Article.objects.create(title='关联一波', type=1, school_id=1)
    article.tag.add(tag)
    return HttpResponse('ok')


def test_json(request):
    # 时间格式一定要先进行转成字符串不然json解析不了
    # JsonResponse其实就是HttpResponse的子类
    query_set = models.Article.objects.all().values('id', 'title', 'create_time', 'type', 'school__name')
    for i in query_set:
        i['create_time'] = i['create_time'].strftime('%Y-%m-%d')
    data = json.dumps(list(query_set), ensure_ascii=False)
    print(data)
    return JsonResponse(data, safe=False)


class DBG(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    create_time = serializers.DateTimeField()
    type = serializers.IntegerField()
    school = serializers.CharField(source='school.name')


class CYM(serializers.Serializer):

    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = models.Article
        fields = '__all__'
        depth = 1


def article_list(request):
    query_set = models.Article.objects.all()
    xbg = CYM(query_set, many=True)
    print(xbg.data)
    return JsonResponse(xbg.data, safe=False)