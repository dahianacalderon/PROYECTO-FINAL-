from django.shortcuts import render, redirect

# Users (login, register)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'El correo y/o la contraseña estan mal ingresados o no existen!')
    return render(request, 'registration/login.html')

def register(request):
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
        else:
            messages.error(request, 'Hubo un fallo en el registro debido a un error en el registro vuelvelo a hacer porfavor!')
    return render(request, 'registration/register.html',{'register_form' : register_form})