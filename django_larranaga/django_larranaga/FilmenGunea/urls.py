from django.urls import path
from . import views

app_name = "filmGunea"

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login')
]