from django.urls import include, path, re_path
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('external/', views.external, name='external'),
    path('search/', views.search, name='search'),
]

