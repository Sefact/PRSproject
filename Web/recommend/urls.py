from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('like', views.like, name="like"),
    path('like/<int:like_id>', views.ldetail, name="ldetail"),
    path('recommend', views.recommend, name="recommend"),
    path('recommend/<int:recommend_id>', views.rdetail, name="rdetail"),
    path('editor', views.editor, name="editor"),
    path('editor/<int:editor_id>', views.edetail, name="edetail"),
    path('area', views.area, name="area"),
    path('area/seoul', views.seoul, name="seoul"),
    path('area/seoul/<int:seoul_id>', views.seoul_detail, name="seoul_detail"),
    path('area/incheon', views.incheon, name="incheon"),
    path('area/incheon/<int:incheon_id>', views.incheon_detail, name="incheon_detail"),
    path('area/busan', views.busan, name="busan"),
    path('area/busan/<int:busan_id>', views.busan_detail, name="busan_detail"),
    path('area/gwanggu', views.gwanggu, name="gwanggu"),
    path('area/gwanggu/<int:gwanggu_id>', views.gwanggu_detail, name="gwanggu_detail"),
    path('area/daejon', views.daejon, name="daejon"),
    path('area/daejon/<int:daejon_id>', views.daejon_detail, name="daejon_detail"),
    path('area/gangwon', views.gangwon, name="gangwon"),
    path('area/gangwon/<int:gangwon_id>', views.gangwon_detail, name="gangwon_detail"),
]