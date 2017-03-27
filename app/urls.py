from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
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
    url(r'^contact/', views.contact, name='contact'),
    url(r'^schemes/create$', SchemeCreate.as_view(), name='CreatePost'),
    url(r'^schemes/(?P<slug>[\w-]+)/$', SchemeDetailedList.as_view(), name='DetailedView'),
    url(r'^schemes/(?P<slug>[\w-]+)/edit/$', SchemeUpdateList.as_view(), name='Edit'),
    url(r'^schemes/(?P<slug>[\w-]+)/delete/$', SchemeDeleteList.as_view(), name='Delete'),
    url(r'^schemes/$', SchemeList.as_view(), name='list'),
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),

]

