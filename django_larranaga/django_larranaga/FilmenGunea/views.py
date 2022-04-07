from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login as login_auth
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render_to_response('FilmenGunea/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if authenticate(username, password) is not None:
            if user.is_active:
                login_auth(request, user)
                return HttpResponseRedirect('menus/')
            else:
                messages.error(request, "Ezin izan da kontuan sartu. Kontua desgaituta dago.")
        else:
            messages.error(request, "Ezin izan da kontuan sartu. Erabiltzaile izen edo pasahitz okerra.")
    form = LoginForm()
    return render_to_response('FilmenGunea/login.html', {'form':form})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username, password1, password2)
            user.save()
            login(request, user)
            messages.success(request, "Zuzen erregistratu zara.")
            return redirect('FilmenGunea/main.html')
        messages.error(request, "Ezin izan da erregistratu. Datuak ez dira baliozkoak.")
    form = RegisterForm()
    return render_to_response('FilmenGunea/register.html', {'form':form})

def main(request):
    return render_to_response('FilmenGunea/froga.html')