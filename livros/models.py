from django.db import models
import uuid


class Livro(models.Model):
    GENEROS = [
        ('Ficcao', 'Ficção'),
        ('NaoFiccao', 'Não-Ficção'),
        ('Romance', 'Romance'),
        ('Ciencia', 'Ciência'),
        ('Biografia', 'Biografia'),
        ('Fantasia', 'Fantasia'),
        ('Terror', 'Terror'),
    ]

    titulo = models.CharField(max_length=255, verbose_name="Título do Livro")
    autor = models.CharField(max_length=255, verbose_name="Autor")
    isbn = models.CharField(max_length=13, unique=True, editable=False, verbose_name="ISBN")
    editora = models.CharField(max_length=255, verbose_name="Editora")
    ano_publicacao = models.PositiveIntegerField(verbose_name="Ano de Publicação")
    genero = models.CharField(max_length=50, choices=GENEROS, verbose_name="Gênero")
    quantidade_total = models.PositiveIntegerField(verbose_name="Quantidade Total")
    quantidade_disponivel = models.PositiveIntegerField(verbose_name="Quantidade Disponível", default=0)
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.isbn:
            self.isbn = str(uuid.uuid4().int)[:13] # Gera um ISBN aleatório de 13 dígitos

        if self.quantidade_disponivel > self.quantidade_total:
            self.quantidade_disponivel = self.quantidade_total
        super().save(*args, **kwargs)
