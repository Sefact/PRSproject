from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('tag', views.tag, name="tag"),
   path('cafe', views.cafe, name="cafe"),
   path('cafe/<int:cafe_id>', views.cdetail, name="cdetail"),
   path('art', views.art, name="art"),
   path('art/<int:art_id>', views.artdetail, name="artdetail"),
   path('food', views.food, name="food"),
   path('food/<int:food_id>', views.fooddetail, name="fooddetail"),
   path('theater', views.theater, name="theater"),
   path('theater/<int:theater_id>', views.theaterdetail, name="theaterdetail"),
   path('escape', views.escape, name="escape"),
   path('escape/<int:escape_id>', views.escapedetail, name="escapedetail"),
   path('travle', views.travle, name="travle"),
   path('travle/<int:travle_id>', views.travledetail, name="travledetail"),
]