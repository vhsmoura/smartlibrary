from django.shortcuts import render
from .models import Livro
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    livros = Livro.objects.all()
    return render(request, 'index.html', {'livros': livros})

def home(request):
    todos_livros = Livro.objects.all()
    disponiveis = todos_livros.filter(aluno__isnull=True)  # Sem aluno
    emprestados = todos_livros.filter(aluno__isnull=False)  # Com aluno
    return render(request, 'index.html', {
        'livros_disponiveis': disponiveis,
        'livros_emprestados': emprestados
    })

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/admin/')
        messages.error(request, 'Login inválido')
    return render(request, 'login.html')