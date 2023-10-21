from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse 
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def welcome_next(request):
    return render(request, 'welcome_next.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'User Name already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/query')
        else:
            messages.info(request, 'User not found')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def customer_care(request):
    return render(request, 'customer_care.html')
