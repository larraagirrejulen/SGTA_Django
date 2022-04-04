from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='index'),
    path('register/', views.register, name='index'),
    path('login/', views.login, name='index')
]