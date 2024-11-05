from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
import datetime
from django.contrib import messages
from .models import Livro
from emprestimo.models import Emprestimo
from .form import LivroForm
from django.contrib.auth.decorators import login_required, permission_required

def home(request):
    now = datetime.datetime.now()
    return render(request, 'livros/home.html')


def listagem(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listagem.html', {'livros': livros})

@login_required
def solicitar_emprestimo(request):
    if request.method == 'POST':
        livro_id = request.POST.get('livro_id')
        livro = get_object_or_404(Livro, id=livro_id)
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