from django.conf.urls import url, include
from django.contrib import admin

from app import views
from .views import (
    ProfileDetailedList,
    ProfileList,
    ProfileUpdateList,
    ProfileCreate,
    )
from django.views.generic import ListView, DetailView
from app.models import Post

urlpatterns = [
    url(r'^profile/create/$', ProfileCreate.as_view(), name='CreateProfile'),
    url(r'^profile/(?P<user>\d+)/$', ProfileDetailedList.as_view(), name='DetailedViewProfile'),
    # url(r'^profile/(?P<user>\d+)/edit/$', ProfileUpdateList.as_view(), name='EditProfile'),
    # url(r'^profile/$', ProfileList.as_view(), name='list'),
    url(r'^$', ProfileList.as_view(), name='Home')
]

