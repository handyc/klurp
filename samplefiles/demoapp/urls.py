from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('bibliography/', views.bibliography, name='bibliography'),
    path('members/', views.members, name='members'),
    path('news/', views.news, name='news'),
    path('resources/', views.resources, name='resources'),
    path('search/', views.search, name='search'),
]
