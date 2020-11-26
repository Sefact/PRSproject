from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blike, Beditor, LikeComment
from .forms import CommentForm

def home(request):
    blikes = Blike.objects
    beditors = Beditor.objects
    return render(request, 'home.html', {'blikes': blikes, 'beditors': beditors})

def beditordetail(request, beditor_id):
    beditor_detail = get_object_or_404(Beditor, pk=beditor_id)
    return render(request, 'beditor_detail.html', {'beditor': beditor_detail})

def introduce(request):
    return render(request, 'introduce.html')

def contact(request):
    return render(request, 'contact.html')

def blog_like_detail(request, blike_id):
    blike = get_object_or_404(Blike, pk=blike_id)
    #만약 post일때만 댓글 입력에 관한 처리를 더한다.
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.instance.author_id = request.user.id
        comment_form.instance.blike_id = blike_id
        if comment_form.is_valid():
            comment = comment_form.save()

    #models.py에서 document의 related_name을 comments로 해놓았다.

    comment_form = CommentForm()
    like_comments = blike.like_comments.all()

    return render(request, 'blike_detail.html', {'blike':blike, "like_comments":like_comments, "comment_form":comment_form})
# Create your views here.