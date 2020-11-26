from django.shortcuts import render, get_object_or_404, redirect
from .models import Cafe, Art, Food, Theater, Escape, Travle

def tag(request):
    return render(request, 'tag.html')

def cafe(request):
    cafes = Cafe.objects # 쿼리셋 # 메소드
    return render(request, 'cafe.html', {'cafes': cafes})

def cdetail(request, cafe_id):
    cafe_detail = get_object_or_404(Cafe, pk=cafe_id)
    return render(request, 'cdetail.html', {'cafe': cafe_detail})

def art(request):
    arts = Art.objects # 쿼리셋 # 메소드
    return render(request, 'art.html', {'arts': arts})

def artdetail(request, art_id):
    art_detail = get_object_or_404(Art, pk=art_id)
    return render(request, 'artdetail.html', {'art': art_detail})

def food(request):
    foods = Food.objects
    return render(request, 'food.html', {'foods': foods})

def fooddetail(request, food_id):
    food_detail = get_object_or_404(Food, pk=food_id)
    return render(request, 'fooddetail.html', {'food': food_detail})

def theater(request):
    theaters = Theater.objects
    return render(request, 'theater.html', {'theaters': theaters})

def theaterdetail(request, theater_id):
    theater_detail = get_object_or_404(Theater, pk=theater_id)
    return render(request, 'theaterdetail.html', {'theater': theater_detail})

def escape(request):
    escapes = Escape.objects
    return render(request, 'escape.html', {'escapes': escapes})

def escapedetail(request, escape_id):
    escape_detail = get_object_or_404(Escape, pk=escape_id)
    return render(request, 'escapedetail.html', {'escape': escape_detail})

def travle(request):
    travles = Travle.objects
    return render(request, 'travle.html', {'travles': travles})

def travledetail(request, travle_id):
    travle_detail = get_object_or_404(Travle, pk=travle_id)
    return render(request, 'travledetail.html', {'travle': travle_detail})

# Create your views here.