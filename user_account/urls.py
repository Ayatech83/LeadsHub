from django.conf.urls import url
from .views import (login, auth_view,)

urlpatterns = [
    url(r'^auth/$', auth_view, name='auth'),
    url(r'^login/$', login, name='login'),
    url(r'^subscribe/$', login, name='login'),
    ]