from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as user_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import Profile

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
        return redirect('blog:home')
    else:
        form = CustomUserCreationForm() # 비어있는 회원가입 폼을 생성한다.
        return render(request, 'accounts/form.html', {'form': form})
    	# forms.html 파일을 렌더한다. 이때 위에서 생성한 회원가입 폼을 'form'이라는 이름으로 함께 보낸다.(딕셔너리)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 회원가입과 다르게 맨 앞의 인자로 request가 들어간다.
        if form.is_valid():
            user_login(request, form.get_user())
            return redirect('blog:home')
        return redirect('accounts:login')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/form.html', {'form': form})

def logout(request):
    user_logout(request)
    return redirect('blog:home')

# Create your views here.