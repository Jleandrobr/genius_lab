from django.urls import path
from .views import listagem, cadastro_emprestimo, devolver_livro, aprovar_emprestimo, recusar_emprestimo, filtros_emprestimos

urlpatterns = [
    path("", listagem, name="listagem_emprestimo"),
    path("listagem/", filtros_emprestimos, name="filtros_emprestimos"),
    path("cadastro/", cadastro_emprestimo, name="cadastro_emprestimo"),
    path("devolver_livro/", devolver_livro, name="devolver_livro"),
    path("aprovar/", aprovar_emprestimo, name="aprovar_emprestimo"),
    path("recusar/", recusar_emprestimo, name="recusar_emprestimo"),
]