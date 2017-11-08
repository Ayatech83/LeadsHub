from django.conf.urls import url
from .views import (subscribe_view,)

urlpatterns = [
    url(r'^subscribe/$', subscribe_view, name='subscribe'),
    ]