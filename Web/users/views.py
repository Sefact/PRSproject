from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
from .models import Users

def register(request):

    if request.method == 'GET':
        return render(request, 'blog/register.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('re-password', None)
        useremail = request.POST.get('useremail', None)
        errorMsg = {}

        if not (username and useremail and password and repassword):
            errorMsg['error'] = "모든 값을 입력해야 합니다."
        elif password != repassword:
            errorMsg['error'] = "비밀번호가 다릅니다."
        else:
            user = Users(
                username = username,
                password = make_password(password),
                useremail = useremail
            )
            user.save()

        return render(request, 'blog/register.html', errorMsg)

def login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        #정상적인 데이터인지 확인
        if form.is_valid(): #forms.py에 정의한 clean 메소드대로 검증한다.
            #로그인 session 추가
            request.session['user'] = form.user_id #매칭된 fuser모델의 pk를 세션.user로 추가

            return redirect('/') #루트 페이지로 리다이렉트
    else:
        form = LoginForm()
    return render(request,'blog/login.html',{'form':form}) #응답 데이터 res_data 전달

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

# Create your views here.
