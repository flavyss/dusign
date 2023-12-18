from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_dj
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/cadastro.html')
    

@login_required(login_url="/login/")
def home(request):
    return HttpResponse('home')
