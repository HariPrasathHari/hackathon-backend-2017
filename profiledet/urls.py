from django.conf.urls import url, include
from django.contrib import admin
from app import views
from .views import (
    ProfileDetailedList,
    ProfileList,
    ProfileUpdateList,
    ProfileDeleteList,
    ProfileCreate,
    )
from django.views.generic import ListView, DetailView
from app.models import Post

urlpatterns = [
    #url(r'^profile/(?P<pk>\d+)/$', ProfileDetailedList.as_view(), name='Detailedview'),
    url(r'^profile/create$', ProfileCreate.as_view(), name='createpost'),
    url(r'^profile/(?P<pk>\d+)/$', ProfileDetailedList.as_view(), name='Detailed'),
    url(r'^profile/(?P<pk>\d+)/edit/$', ProfileUpdateList.as_view(), name='Edit'),
    url(r'^profile/(?P<pk>\d+)/delete/$', ProfileDeleteList.as_view(), name='Delete'),
    # url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name='app/Post.html')),
    url(r'^profile/$', ProfileList.as_view(), name='list'),
    # url(r'^profile/$',ListView.as_view(queryset=(Post.objects.all().order_by("-date")[:25]),template_name="app/blog.html")),
    url(r'^$', ProfileList.as_view(),name='Home')
]
