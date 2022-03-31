from django.shortcuts import render_to_response
from django.http import HttpResponse
from .forms import LoginForm


def index(request):
    form = LoginForm()
    return render_to_response('FilmenGunea/index.html', {'form':form})