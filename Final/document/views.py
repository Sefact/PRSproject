from django.shortcuts import render, redirect, get_object_or_404
from .models import Document, Comment
from .forms import CommentForm


def document(request):
    documents = Document.objects
    return render(request, 'document.html', {'documents': documents})

def document_detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    #만약 post일때만 댓글 입력에 관한 처리를 더한다.
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.instance.author_id = request.user.id
        comment_form.instance.document_id = document_id
        if comment_form.is_valid():
            comment = comment_form.save()

    #models.py에서 document의 related_name을 comments로 해놓았다.

    comment_form = CommentForm()
    comments = document.comments.all()

    return render(request, 'document_detail.html', {'document':document, "comments":comments, "comment_form":comment_form})
# Create your views here.