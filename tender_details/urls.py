from django.conf.urls import url
from .views import (tender_view,)

urlpatterns = [
    url(r'^$', tender_view, name='tender'),
    ]