from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Você entrou!")
                return redirect('home')
            else:
                messages.error(request, "Usuário ou senha inválidos. Por favor, tente novamente.")
        else:
            messages.error(request, "Usuário e senha são obrigatórios.")
    
    return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Você foi desconectado!")

    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})
