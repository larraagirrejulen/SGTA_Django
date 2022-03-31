from django.shortcuts import render_to_response
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login as auth_login


def index(request):
    form = LoginForm()
    return render_to_response('FilmenGunea/index.html', {'form':form})

def login(request):
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
            
    else:
        # Errore-mezua bueltatu: 'login desegokia'.


def erregistratu(request):
    form = RegisterForm()
    return render_to_response('FilmenGunea/register.html', {'form':form})

def menua(request):
    return render_to_response('FilmenGunea/froga.html')