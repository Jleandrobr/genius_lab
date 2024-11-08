from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth.models import User

from emprestimo.form import EmprestimoForm
from .models import Livro
from .models import Emprestimo
from django.core.paginator import Paginator

@login_required(login_url='login')
def listagem(request):
    if request.user.is_superuser:
        emprestimos = Emprestimo.objects.all()
    else:
        emprestimos = Emprestimo.objects.filter(usuario=request.user)

    emprestimos = emprestimos.order_by('-data_emprestimo') # exibe os emprestimos mais recentes primeiro

    paginator = Paginator(emprestimos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'emprestimos/listagem.html', {'page_obj': page_obj})

@login_required(login_url='login')
def filtros_emprestimos(request):
    usuarios = User.objects.all()

    if request.user.is_superuser:
        emprestimos = Emprestimo.objects.all()
    else:
        emprestimos = Emprestimo.objects.filter(usuario=request.user)

    nome_livro = request.GET.get('nome_livro', '')
    status = request.GET.get('status', '')
    usuario_id = request.GET.get('usuario', '')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')

    if nome_livro:
        emprestimos = emprestimos.filter(livro__titulo__icontains=nome_livro)
    
    if status:
        emprestimos = emprestimos.filter(status=status)

    if usuario_id and request.user.is_superuser:
        emprestimos = emprestimos.filter(usuario_id=usuario_id)

    if data_inicial:
        data_inicial = datetime.datetime.strptime(data_inicial, "%Y-%m-%d")
        emprestimos = emprestimos.filter(data_emprestimo__gte=data_inicial)
    
    if data_final:
        data_final = datetime.datetime.strptime(data_final, "%Y-%m-%d")
        emprestimos = emprestimos.filter(data_emprestimo__lte=data_final)
    
    emprestimos = emprestimos.order_by('-data_emprestimo') # exibe os emprestimos mais recentes primeiro
                                         
    paginator = Paginator(emprestimos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'emprestimos/listagem.html', {
        'page_obj': page_obj,
        'usuarios': usuarios,
    })

@login_required
def cadastro_emprestimo(request):
    form = EmprestimoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listagem_emprestimo')
    
    return render(request, 'emprestimos/cadastro.html', {'form': form})

@login_required
def devolver_livro(request):
    if request.method == 'POST':
        emprestimo_id = request.POST.get('emprestimo_id')
        observacao = request.POST.get('observacao')
        emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
        emprestimo.observacao = observacao
        emprestimo.registrar_devolucao()
        
        messages.success(request, "Devolução registrada com sucesso!")
        return redirect('listagem_emprestimo')


@login_required()
def aprovar_emprestimo(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            emprestimo_id = request.POST.get('emprestimo_id')
            emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
            
            emprestimo.aprovar_emprestimo()
            
            messages.success(request, "Empréstimo aprovado com sucesso!")
            return redirect('listagem_emprestimo')
    else:
        return HttpResponse("Você não tem permissão para acessar esta página.")
    
@login_required
def recusar_emprestimo(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            emprestimo_id = request.POST.get('emprestimo_id')
            emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
            
            emprestimo.recusar_emprestimo()
            
            messages.success(request, "Empréstimo recusado com sucesso!")
            return redirect('listagem_emprestimo')
    else:
        return HttpResponse("Você não tem permissão para acessar esta página.")

