from django.conf.urls import url


from news import views


urlpatterns = [
    url('^login/', views.login, name='login'),
    url('^index/', views.index, name='index'),
    url('^logout/', views.Logout.as_view(), name='logout'),
    url('^insert/', views.insert_into, name='insert'),
    url('^test_json/', views.test_json, name='test_json'),

]