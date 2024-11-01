from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
import datetime

from emprestimo.form import EmprestimoForm
from .models import Livro
from .models import Emprestimo

def listagem(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimos/listagem.html', {'emprestimos': emprestimos})

def cadastro_emprestimo(request):
    form = EmprestimoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listagem_emprestimo')
    
    return render(request, 'emprestimos/cadastro.html', {'form': form})

def devolver_livro(request):
    if request.method == 'POST':
        emprestimo_id = request.POST.get('emprestimo_id')
        emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
        
        emprestimo.registrar_devolucao()
        
        messages.success(request, "Devolução registrada com sucesso!")
        return redirect('listagem_emprestimo')

