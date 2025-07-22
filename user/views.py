from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def user_register(request):    
    return render(request, 'user/register.html')

def user_save(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')     
        email = request.POST.get('email')

        #senhas são iguais
        if password != password2:
           messages.error(request, 'As senhas não coincidem.')
           return redirect('user:register')
    

        # Verifica se o usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
            return redirect('user:register')

        # Cria o usuário
        User.objects.create_user(username=username, password=password, email=email)

        messages.success(request, 'Cadastro realizado com sucesso. Faça login.')
        return redirect('login')  # ou a URL que você usa para o login

    return redirect('user:register')  # Se não for POST, redireciona de volta

        