"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('profiledet.urls')),
    url(r'^users/', include('abca.urls')),
    url(r'^app/',include('app.urls', namespace='postss-api')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    #url(r'^schemes/',views.schemeList.as_view()),
    url(r'^',include('app.urls'),name='app-1'),
]

urlpatterns=format_suffix_patterns(urlpatterns)