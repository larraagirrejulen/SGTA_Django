from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from FilmenGunea.models import Filma, Bozkatzailea


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
            return redirect('../login')
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
    paginator = Paginator(film_list, 5)
    page = request.GET.get('page')
    try:
        filmak = paginator.page(page)
    except PageNotAnInteger:
        filmak = paginator.page(1)
    except EmptyPage:
        filmak = paginator.page(paginator.num_pages)
    return render(request, 'FilmenGunea/filmak.html', {"filmak": filmak})


@login_required(login_url='../')
def bozkatu(request):

    film_list = Filma.objects.all()
    if request.method == "POST":
        filmaIzena = request.POST.get('dropFilm')
        filma=Filma.objects.get(izenburua=filmaIzena)
        er=request.user

        bozkaDenak = Bozkatzailea.objects.all()

        for boz in bozkaDenak:
            if Bozkatzailea.objects.filter(gogokofilmak=filma,erabiltzailea_id=er.id).exists():
                messages.error(request, "Dagoeneko bozkatu duzu pelikula hau")
                return render(request, 'FilmenGunea/bozkatu.html', {"filmak": film_list})

        b1 = Bozkatzailea(erabiltzailea_id=er)
        b1.save()
        b1.gogokofilmak.add(filma)

        messages.success(request, "Ondo bozkatu da")

    return render(request, 'FilmenGunea/bozkatu.html', {"filmak": film_list})

@login_required(login_url='../')
def zaleak(request):
    if request.method == "POST":

        filmIzena = request.POST.get('dropFilm')

        filma = Filma.objects.get(izenburua=filmIzena)

        usr = filma.bozkatzailea_set.all()

        film_list = Filma.objects.all()
        return render(request, 'FilmenGunea/zaleak.html', {"bozkak": usr,"filmak": film_list})

    else:
        film_list = Filma.objects.all()
        return render(request, 'FilmenGunea/zaleak.html', {"filmak": film_list})