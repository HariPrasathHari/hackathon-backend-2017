from django.conf.urls import url, include
from django.contrib import admin

from .views import StatusList



urlpatterns = [
    url(r'^', StatusList.as_view(), name='List'),
    ]