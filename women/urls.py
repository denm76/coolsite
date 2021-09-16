from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/<int:catid>/', views.categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive),
]
