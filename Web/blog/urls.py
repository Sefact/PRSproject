from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<int:blike_id>', views.blog_like_detail, name="blog_like_detail"),
    path('editor/<int:beditor_id>', views.beditordetail, name="beditordetail"),
    path('introduce', views.introduce, name='introduce'),
    path('contact', views.contact, name='contact'),
]