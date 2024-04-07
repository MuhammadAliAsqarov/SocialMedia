
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import MyUser


def login_view(request):
    d = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            d['error'] = "Invalid username or password"
    return render(request, 'login.html', context=d)


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('/auth/login')


def register_view(request):
    d={}
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if not User.objects.filter(username=username).exists() and password1 == password2:
            user=User.objects.create(username=username,password=make_password(password1))
            user.save()
            my_user=MyUser.objects.create(user=user)
            my_user.save()
            return redirect('/auth/login')
        d['error'] = "Username is already taken or passwords don't match"
    return render(request, 'register.html',context=d)
