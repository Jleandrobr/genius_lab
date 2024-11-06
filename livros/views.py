from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
import datetime
from django.contrib import messages
from .models import Livro
from emprestimo.models import Emprestimo
from .form import LivroForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator

def home(request):
    now = datetime.datetime.now()
    return render(request, 'livros/home.html')


def listagem(request):
    livros = Livro.objects.all()
    paginator = Paginator(livros, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'livros/listagem.html', {'page_obj': page_obj})

def filtros_livros(request):
    livros = Livro.objects.all()

    # captura os parametros de busca
    titulo = request.GET.get('titulo', '')
    autor = request.GET.get('autor', '')
    ano_publicacao = request.GET.get('ano_publicacao', '')
    editora = request.GET.get('editora', '')

    # aplica o filtro caso os campos estejam preenchidos
    if titulo:
        livros = livros.filter(titulo__icontains=titulo)
    if autor:
        livros = livros.filter(autor__icontains=autor)
    if ano_publicacao:
        livros = livros.filter(ano_publicacao=ano_publicacao)
    if editora:
        livros = livros.filter(editora__icontains=editora)

    paginator = Paginator(livros, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'livros/listagem.html', {'page_obj': page_obj})

@login_required
def solicitar_emprestimo(request):
    if request.method == 'POST':
        livro_id = request.POST.get('livro_id')
        livro = get_object_or_404(Livro, id=livro_id)

        if not livro.esta_disponivel():
            messages.error(request, "Este livro não está disponível para empréstimo.")
            return redirect('listagem_emprestimo')
        
        emprestimo = Emprestimo(livro=livro, usuario=request.user)
        emprestimo.save()
        
        messages.success(request, "Empréstimo solicitado com sucesso!")
        return redirect('listagem_emprestimo')

@login_required
def cadastro_livro(request):
    form = LivroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listagem_livro')

    return render(request, 'livros/cadastro.html', {'form': form})