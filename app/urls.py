from django.conf.urls import url, include
from django.contrib import admin
from app import views
from .views import (
    SchemeDetailedList,
    SchemeList,
    SchemeUpdateList,
    SchemeDeleteList,
    SchemeCreate,
    )
from django.views.generic import ListView, DetailView
from app.models import Post

urlpatterns = [
    # url(r'^',views.hello,name='hello'),
    url(r'^home/', views.home,name='home'),
    url(r'^contact/', views.contact, name='contact'),
    #url(r'^schemes/(?P<pk>\d+)/$', SchemeDetailedList.as_view(), name='Detailedview'),
    url(r'^schemes/create$', SchemeCreate.as_view(), name='CreatePost'),
    url(r'^schemes/(?P<title>[\w-]+)/$', SchemeDetailedList.as_view(), name='DetailedView'),
    url(r'^schemes/(?P<title>[\w-]+)/edit/$', SchemeUpdateList.as_view(), name='Edit'),
    url(r'^schemes/(?P<title>[\w-]+)/delete/$', SchemeDeleteList.as_view(), name='Delete'),
    # url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name='app/Post.html')),
    url(r'^schemes/$', SchemeList.as_view(), name='list'),
    # url(r'^schemes/$',ListView.as_view(queryset=(Post.objects.all().order_by("-date")[:25]),template_name="app/blog.html")),
    url(r'^$', views.home, name='home'),
]
