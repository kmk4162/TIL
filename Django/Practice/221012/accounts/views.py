from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login # 함수 이름과 겹치니까 auth_login으로!
from django.contrib.auth import logout as auth_logout # 로그아웃도 마찬가지
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    users = get_user_model().objects.all()
    context = {
        'users' : users,
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

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
