from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
# Create your views here.


from blog.models import Article
from blog.models import UserInfo


def index(request):
    article_list = Article.objects.all()
    print(article_list)
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
    article_lists = Article.objects.filter(user__username=username)
    return render(request, 'home_site.html', {'user': user, 'article_list': article_lists})
