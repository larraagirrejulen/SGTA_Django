from django.shortcuts import render_to_response
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm


def index(request):
    form = LoginForm()
    return render_to_response('FilmenGunea/index.html', {'form':form})

def erregistratu(request):
    form = RegisterForm()
    return render_to_response('FilmenGunea/index.html', {'form':form})

def menua(request):
    return render_to_response('FilmenGunea/froga.html')