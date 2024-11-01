from django.urls import path
from .views import home, listagem, cadastro_livro

urlpatterns = [
    path("home/", home),
    path("", listagem, name="listagem_livro"),
    path("cadastro/", cadastro_livro, name="cadastro_livro"),
]