from django.conf.urls import url, include
from django.contrib import admin

from .views import StatusList, StatusDetailedList, StatusEdit

urlpatterns = [
    url(r'^$', StatusList.as_view(), name='List'),
    url(r'^(?P<pk>\d+)/$', StatusDetailedList.as_view(), name='Detail'),
    url(r'^(?P<pk>\d+)/edit$', StatusEdit.as_view(), name='Edit'),
    ]