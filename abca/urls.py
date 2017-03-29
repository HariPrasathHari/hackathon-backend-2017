from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    GetUserID,
    )

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^fetchid/$', GetUserID.as_view(), name='GetID'),
]

