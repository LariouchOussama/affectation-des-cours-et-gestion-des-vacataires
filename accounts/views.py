from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import Group









# Create your views here.

def Index(request):
    return render(request, 'accounts/login.html')

def home(request):

    vacataire_group = Group.objects.get(name='Vacataire')
    employe_group =  Group.objects.get(name='Vacataire')
    vacataires = vacataire_group.user_set.all()
    nbre_v = vacataire_group.user_set.count()
    employe = employe_group.user_set.all()

    return render(request,'accounts/dashboard.html', {'vacataires': vacataires, 'employe': employe, 'n': nbre_v} )

