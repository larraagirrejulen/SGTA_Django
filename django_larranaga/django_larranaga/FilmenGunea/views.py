from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'FilmenGunea/index.html')

def login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                auth_login(request, user)

                return redirect('../main')
            else:
                messages.error(request, "Ezin izan da kontuan sartu. Kontua desgaituta dago.")
        else:
            messages.error(request, "Ezin izan da kontuan sartu. Erabiltzaile izen edo pasahitz okerra.")
    form = LoginForm()
    return render(request, 'FilmenGunea/login.html', {'form':form})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            auth_login(request, user)
            return redirect('../main')
        messages.error(request, "Ezin izan da erregistratu. Datuak ez dira baliozkoak.")
    form = RegisterForm()
    return render(request, 'FilmenGunea/register.html', {'form':form})

def logout_eskaera(request):
    logout(request)
    return redirect('../')

@login_required(login_url='../')
def main(request):
    return render(request, 'FilmenGunea/main.html', {'user':request.user})

@login_required(login_url='../')
def filmak(request):
    film_list = Filma.objects.all()
    paginator = Paginator(film_list, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        filmak = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        filmak = paginator.page(paginator.num_pages)
    return render(request, 'FilmenGunea/filmak.html', {"filmak": filmak})

@login_required(login_url='../')
def bozkatu(request):
    return render(request, 'FilmenGunea/bozkatu.html')

@login_required(login_url='../')
def zaleak(request):
    return render(request, 'FilmenGunea/zaleak.html')