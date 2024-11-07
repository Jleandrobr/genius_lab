from django.urls import path
from .views import home, listagem, cadastro_livro, solicitar_emprestimo, filtros_livros, livro_update, livro_inativar

urlpatterns = [
    path("home/", home),
    path("", listagem, name="listagem_livro"),
    path("listagem/", filtros_livros, name="filtros_livros"),
    path("update/<int:id>", livro_update, name="update_livro"),
    path("inativar/<int:id>", livro_inativar, name="inativar_livro"),
    path("cadastro/", cadastro_livro, name="cadastro_livro"),
    path("solicitar_emprestimo/", solicitar_emprestimo, name="solicitar_emprestimo"),
]