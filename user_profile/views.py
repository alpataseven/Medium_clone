from django.shortcuts import render

def login_view(request):
    context = {}
    return render(request, 'user_profile/login.html', context)
