from django.conf.urls import url


from blog import views


urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^home_work/', views.home_work, name='home_work'),
    url(r'(?P<username>\w+)', views.home_site),
    url(r'.', views.index),

]