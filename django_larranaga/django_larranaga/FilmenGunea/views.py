from django.shortcuts import render_to_response
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User


def index(request):
    return render_to_response('FilmenGunea/index.html')

def login(request):
    form = LoginForm()
    return render_to_response('FilmenGunea/login.html', {'form':form})

def login_request(request):
    erab = request.POST['username']
    pasa = request.POST['password']
    user = authenticate(username=erab, password=pasa)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Berbideratu login ondorengo orri batera.
            return HttpResponseRedirect('menus/')
        else:
            # Errore-mezua bueltatu: 'kontua desgaituta'.
            return HttpResponse("<h1>Errorea: kontua desgaituta dago</h1>")
    else:
        # Errore-mezua bueltatu: 'login desegokia'.
        return HttpResponse("<h1>Errorea: erabiltzaile edo pasahitz okerra</h1>");

def register(request):
    form = RegisterForm()
    return render_to_response('FilmenGunea/register.html', {'form':form})

def register_request(request):
    erab = request.POST['username']
    pasa = request.POST['password']
    user = authenticate(username=erab, password=pasa)
    if user is not None:
        return render_to_response('FilmenGunea/register.html', {'emaitza':"<h1>Errorea: erabiltzailea dagoeneko erregistratuta dago</h1>"})
    else:
        erab = User.objects.create_user(erab, pasa)
        return render_to_response('FilmenGunea/register.html', {'emaitza':"<h1>Erabiltzailea zuzen erregistratu da</h1>"})

def main(request):
    return render_to_response('FilmenGunea/froga.html')