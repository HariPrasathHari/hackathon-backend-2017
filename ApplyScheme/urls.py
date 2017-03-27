from django.conf.urls import url, include
from django.contrib import admin
from app import views
from django.views.generic import ListView, DetailView
from ApplyScheme.models import AppliedSchemes
from .views import AppliedSchemeCreate
urlpatterns = [
    url(r'^$', AppliedSchemeCreate.as_view(), name='Apply'),
    # url(r'^/(?P<user>\d+)/$', ProfileCreate.as_view(), name='CreateProfile'),
    # url(r'^profile/(?P<user>\d+)/$', ProfileDetailedList.as_view(), name='DetailedViewProfile'),
    # url(r'^profile/(?P<user>\d+)/edit/$', ProfileUpdateList.as_view(), name='EditProfile'),
    # url(r'^profile/$', ProfileList.as_view(), name='list'),
    # url(r'^$', ProfileList.as_view(), name='Home')
]
