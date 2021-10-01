from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>', views.show_post, name='post'),
    path('category/<int:category_id>', views.show_category, name='category'),
]
