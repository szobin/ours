# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^log/process/$', views.view_api_process_log),
]
