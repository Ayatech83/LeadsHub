from django.conf.urls import url
from .views import (subscribe_view, user_login,)

urlpatterns = [
    url(r'^subscribe/$', subscribe_view, name='subscribe'),
    url(r'^login/$', user_login, name='login'),
    ]