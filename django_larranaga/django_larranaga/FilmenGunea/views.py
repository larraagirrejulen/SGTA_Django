from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

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