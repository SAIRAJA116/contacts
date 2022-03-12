from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginpage(request):
    if(request.method == "POST"):
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email)
        print(password)
        user = authenticate(email=email, password=password)
        if (user is not None):
            login(request, user)
            return redirect("App:dashboard")
        else:
            messages.error(
                request, " email or password are wrong please try again")
            return redirect("App:loginpage")
    return render(request, "App/loginpage.html")


@login_required(login_url="App:loginpage")
def logoutuser(request):
    pass
    logout(request)
    return redirect("App:loginpage")


def signup(request):
    if(request.method == "POST"):
        email = request.POST.get("email")
        name = request.POST.get("name")
        password = request.POST.get("password")
        secret = request.POST.get("secret")
        user = NewUser(email=email, name=name,
                       password=make_password(password), secret=secret)
        user.save()
        return redirect("App:loginpage")
    return render(request, "App/signup.html")


@login_required(login_url="App:loginpage")
def dashboard(request):
    contacts = Contact.objects.filter(user=request.user)
    if(request.method == "POST"):
        name = request.POST.get("name")
        number = request.POST.get("number")
        email = request.POST.get("email")
        contact = Contact(user=request.user, name=name,
                          number=number, email=email)
        contact.save()
        return redirect("App:dashboard")
    return render(request, "App/dashboard.html", {"contacts": contacts})
