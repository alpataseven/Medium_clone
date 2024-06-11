from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, f'{request.user.username} daha önceden giriş yapmışsınız..')
        return redirect('home_view')
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username} giriş yapıldı..')
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)
