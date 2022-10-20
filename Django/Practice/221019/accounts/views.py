from django.shortcuts import render

def login(request):

    return render(request, 'accounts/login.html')

def logout(request):

    return render(request, 'accounts/logout.html')

def detail(request):

    return render(request, 'accounts/detail.html')
