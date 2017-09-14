from django.conf.urls import url
from article import views

urlpatterns = [
	url(r'^1/', views.basic_one, name='basic 1'),
	url(r'^2/', views.template_two, name='template 2'),
	url(r'^3/', views.template_three_simple, name='template 3 simple'),
#	url(r'^articles/all/$', views.articles, name='articles all'),
	url(r'^articles/get/(?P<article_id>\d+)/$', views.article, name='article'),
	url(r'^articles/addlike/(?P<article_id>\d+)/$', views.addlike, name='addlike'),
	url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment, name='addcomment'),	
	url(r'^$', views.articles, name='articles all'),


]