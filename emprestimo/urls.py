from django.urls import path
from .views import listagem, cadastro_emprestimo, devolver_livro

urlpatterns = [
    path("", listagem, name="listagem_emprestimo"),
    path("cadastro/", cadastro_emprestimo, name="cadastro_emprestimo"),
    path("devolver_livro/", devolver_livro, name="devolver_livro"),
]