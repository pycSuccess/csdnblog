from django.conf.urls import url


from blog import views


urlpatterns = [
    url(r'^index/', views.index, name='blog.index'),
    url(r'^login/', views.login, name='blog.login'),
    url(r'^logout/', views.logout, name='blog.logout'),
    url(r'^home_work/', views.home_work, name='blog,home_work'),
    url(r'^(?P<username>\w+)/(?P<condition>category|tag|achrive)/(?P<parmams>.*)', views.home_site,
        name='blog.home_site_params'),
    url(r'^(?P<username>\w+)/', views.home_site, name='blog.home_site'),
    url(r'.', views.index),

]