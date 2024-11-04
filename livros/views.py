from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
import datetime
from .models import Livro
from .form import LivroForm
from django.contrib.auth.decorators import login_required, permission_required

def home(request):
    now = datetime.datetime.now()
    return render(request, 'livros/home.html')


def listagem(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listagem.html', {'livros': livros})

@login_required
def cadastro_livro(request):
    form = LivroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listagem_livro')

    return render(request, 'livros/cadastro.html', {'form': form})