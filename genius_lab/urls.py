"""
URL configuration for genius_lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from livros.views import home, listagem, cadastro_livro
from emprestimo.views import listagem, cadastro_emprestimo, devolver_livro

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home),
    path("", listagem, name="url_listagem"),
    path("cadastro_livro/", cadastro_livro, name="url_cadastro_livro"),
    path("emprestimo/", listagem, name="url_listagem_emprestimo"),
    path("cadastro_emprestimo/", cadastro_emprestimo, name="url_cadastro_emprestimo"),
    path("devolver_livro/", devolver_livro, name="devolver_livro"),
]
