from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.template import loader


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