from django.urls import path
from .views import home, listagem, cadastro_livro, solicitar_emprestimo, filtros_livros

urlpatterns = [
    path("home/", home),
    path("", listagem, name="listagem_livro"),
    path("listagem/", filtros_livros, name="filtros_livros"),
    path("cadastro/", cadastro_livro, name="cadastro_livro"),
    path("solicitar_emprestimo/", solicitar_emprestimo, name="solicitar_emprestimo"),
]