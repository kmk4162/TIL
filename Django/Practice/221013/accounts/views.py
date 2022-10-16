from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        # GET 방식(처음 들어가거나, 새로고침같은)이면 빈 폼으로
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def index(request):
    users = get_user_model().objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)

def detail(request, pk):
    user = get_user_model().objects.get(pk = pk)
    context = {
        'user' : user,
    }
    return render(request, 'accounts/detail.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            # get_user()은 AuthenticationForm의 메서드
            # 유효성 검사를 통과했을 경우에만 로그인한 사용자 객체를 반환
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    # 처음 페이지 들어올때는 이전에 작성했던 그대로 유지해야함
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)
