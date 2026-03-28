from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Livro


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


@login_required
def marcar_devolvido(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.aluno = None
        livro.data_devolucao = None
        livro.save(update_fields=['aluno', 'data_devolucao'])
        messages.success(
            request, f'Livro "{livro.titulo}" marcado como disponível.')
    return redirect('home')
