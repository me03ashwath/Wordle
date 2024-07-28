from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404


def loginPage(request):
    request._messages._queued_messages.clear()
    page = 'Login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'username not found')
        if authenticate(request, username = username, password = password) is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'password wrong')
    
    context = {'page': page}
    return render(request, 'login_signup/login_signup.html', context)

def signupPage(request):
    request._messages._queued_messages.clear()

    page = 'SignUp'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if username is not None and password is not None:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
            else:
                if password != re_password:
                    messages.error(request, 'passwords do not match')
                else:
                    try:
                        user = User.objects.create_user(username=username, password=password)
                        logout(request)
                        return redirect('login')
                    except:
                        messages.error(request, 'error occured during creating account')
            
    context = {'page':page}
    return render(request, 'login_signup/login_signup.html', context)
