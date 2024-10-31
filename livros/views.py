from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
import datetime
from .models import Livro
from .form import LivroForm

def home(request):
    now = datetime.datetime.now()
    return render(request, 'livros/home.html')



def listagem(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listagem.html', {'livros': livros})

def cadastro_livro(request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, 'livros/cadastro.html', {'form': form})
