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
    path('contact/', views.contact, name='contact'),
    path('recommendation1/', views.recommendation1, name='recommendation1'),
    path('recommendation2/', views.recommendation2, name='recommendation2'),
    path('recommendation3/', views.recommendation3, name='recommendation3'),
    path('recommendation4/', views.recommendation4, name='recommendation4'),
]