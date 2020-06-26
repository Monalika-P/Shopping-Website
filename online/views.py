from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth

from online.models import UserRegister
# Create your views here.


def home(request):
    return render(request, 'index.html')


def register(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        lname= request.POST['lname']
        email = request.POST['email']
        password = request.POST['psw']
        phone = request.POST['ph']
        password1 = request.POST['psw-repeat']

        if password != password1:
            messages.info(request, "Password mismatch")
            return redirect('register')

        if UserRegister.objects.filter(email = email).exists():
            messages.info(request, "Email already exists. Please Login")
            return redirect('register')

        elif UserRegister.objects.filter(phone = phone).exists():
            messages.info(request, "User already exists. Please Login")
            return redirect('register')

        else:
            online_user = UserRegister.objects.create( first_name= fname, last_name = lname, email = email, phone = phone)
            online_user.set_password(password)
            online_user.save()
            messages.info(request, "User created")
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        ph = request.POST['ph']
        password = request.POST['psw']
        user = UserRegister.objects.filter(phone=ph).first() # retriving the phone number fromm the db
        user = authenticate(request, phone=ph, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
        else:
            messages.info(request, "Invalid Phone Number or Password")
            return HttpResponseRedirect(reverse('login'))

    else:
        return render(request, 'login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))

def offers(request):
    return render(request, 'offers.html')


def help(request):
    return render(request, 'help.html')
