"""LeadsHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from website.views import (homePage_view, aboutUs_view, network_view,)

urlpatterns = [
    url(r'^$', homePage_view, name='homepage'),
    url(r'^about/$', aboutUs_view, name='about'),
    url(r'^user_account/', include('user_account.urls')),
    url(r'^tenders/', include('tender_details.urls')),
    url(r'^network/$', network_view, name='network'),
    url(r'^admin/', include(admin.site.urls)),
]