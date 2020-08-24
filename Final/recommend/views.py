from django.shortcuts import render, get_object_or_404, redirect
from .models import Like, Recommend, Editor, Area
from .models import Seoul, Incheon, Busan, Gwanggu, Daejon, Gangwon

def like(request):
    likes = Like.objects
    return render(request, 'like.html', {'likes': likes})

def ldetail(request, like_id):
    like_detail = get_object_or_404(Like, pk=like_id)
    return render(request, 'ldetail.html', {'like': like_detail})

def recommend(request):
    recommends = Recommend.objects
    return render(request, 'recommend.html', {'recommends': recommends})

def rdetail(request, recommend_id):
    recommend_detail = get_object_or_404(Recommend, pk=recommend_id)
    return render(request, 'rdetail.html', {'recommend': recommend_detail})

def editor(request):
    editors = Editor.objects
    return render(request, 'editor.html', {'editors': editors})

def edetail(request, editor_id):
    editor_detail = get_object_or_404(Editor, pk=editor_id)
    return render(request, 'edetail.html', {'editor': editor_detail})

def area(request):
    return render(request, 'area.html')

def seoul(request):
    seouls = Seoul.objects
    return render(request, 'area/seoul.html', {'seouls': seouls})

def seoul_detail(request, seoul_id):
    seoul_detail = get_object_or_404(Seoul, pk=seoul_id)
    return render(request, 'area/seoul_detail.html', {'seoul': seoul_detail})

def incheon(request):
    incheons = Incheon.objects
    return render(request, 'area/incheon.html', {'incheons': incheons})

def incheon_detail(request, incheon_id):
    incheon_detail = get_object_or_404(Incheon, pk=incheon_id)
    return render(request, 'area/incheon_detail.html', {'incheon': incheon_detail})

def busan(request):
    busans = Busan.objects
    return render(request, 'area/busan.html', {'busans': busans})

def busan_detail(request, busan_id):
    busan_detail = get_object_or_404(Busan, pk=busan_id)
    return render(request, 'area/busan_detail.html', {'busan': busan_detail})

def gwanggu(request):
    gwanggus = Gwanggu.objects
    return render(request, 'area/gwanggu.html', {'gwanggus': gwanggus})

def gwanggu_detail(request, gwanggu_id):
    gwanggu_detail = get_object_or_404(Gwanggu, pk=gwanggu_id)
    return render(request, 'area/gwanggu_detail.html', {'gwanggu': gwanggu_detail})

def daejon(request):
    daejons = Daejon.objects
    return render(request, 'area/daejon.html', {'daejons': daejons})

def daejon_detail(request, daejon_id):
    daejon_detail = get_object_or_404(Daejon, pk=daejon_id)
    return render(request, 'area/daejon_detail.html', {'daejon': daejon_detail})

def gangwon(request):
    gangwons = Gangwon.objects
    return render(request, 'area/gangwon.html', {'gangwons': gangwons})

def gangwon_detail(request, gangwon_id):
    gangwon_detail = get_object_or_404(Gangwon, pk=gangwon_id)
    return render(request, 'area/gangwon_detail.html', {'gangwon': gangwon_detail})

# Create your views here.