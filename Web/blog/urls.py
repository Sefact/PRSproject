#URLconf file
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('introduce/', views.introduce, name='introduce'),
    path('services/', views.services, name='services'),
    path('services_list1', views.services_list1, name='services_list1'),
    path('contact/', views.contact, name='contact'),
    path('recommendation1/', views.recommendation1, name='recommendation1'),
    path('recommendation1_2/', views.recommendation1_2, name='recommendation1_2'),
    path('recommendation2/', views.recommendation2, name='recommendation2'),
    path('recommendation3/', views.recommendation3, name='recommendation3'),
    path('recommendation4/', views.recommendation4, name='recommendation4'),
    path('index_editor1/', views.index_editor1, name='index_editor1'),
    path('index_editor2/', views.index_editor2, name='index_editor2'),
    path('index_editor3/', views.index_editor3, name='index_editor3'),
    path('recommend3_1/', views.recommend3_1, name='recommend3_1'),
    path('recommend3_2/', views.recommend3_2, name='recommend3_2'),
    path('recommend3_3/', views.recommend3_3, name='recommend3_3'),
    path('recommend3_4/', views.recommend3_4, name='recommend3_4'),
    path('recommend3_5/', views.recommend3_5, name='recommend3_5'),
    path('recommend3_6/', views.recommend3_6, name='recommend3_6'),
]