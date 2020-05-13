from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.template import loader


## Main page views
def index(request):
    template = loader.get_template('blog/index.html')
    now = datetime.now()
    context = {
        'latest_question_list': "test",
        'current_date': now,
    }
    return HttpResponse(template.render(context, request))

def introduce(request):
    return render(request, 'blog/introduce.html')

def services(request):
    return render(request, 'blog/services.html')

def contact(request):
    return render(request, 'blog/faq.html')

def recommendation1(request):
    return render(request, 'blog/recommendation1.html')

def recommendation2(request):
    return render(request, 'blog/recommendation2.html')

def recommendation3(request):
    return render(request, 'blog/recommendation3.html')

def recommendation4(request):
    return render(request, 'blog/recommendation4.html')

## Main Page Editor Recommendation views
def index_editor1(request):
    return render(request, 'blog/index/index_editor1.html')

def index_editor2(request):
    return render(request, 'blog/index/index_editor2.html')

def index_editor3(request):
    return render(request, 'blog/index/index_editor3.html')

## Recommendation One Page Recommendation views
def recommend3_1(request):
    return render(request, 'blog/recommend3/recommend3_1.html')

def recommend3_2(request):
    return render(request, 'blog/recommend3/recommend3_2.html')

def recommend3_3(request):
    return render(request, 'blog/recommend3/recommend3_3.html')

def recommend3_4(request):
    return render(request, 'blog/recommend3/recommend3_4.html')

def recommend3_5(request):
    return render(request, 'blog/recommend3/recommend3_5.html')

def recommend3_6(request):
    return render(request, 'blog/recommend3/recommend3_6.html')

def recommendation1_2(request):
    return render(request, 'blog/recommendation1_2.html')

## Service Page list views
def services_list1(request):
    return render(request, 'blog/services_list1.html')