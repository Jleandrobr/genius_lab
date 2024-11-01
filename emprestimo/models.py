from django.db import models
from livros.models import Livro
from django.utils import timezone


class Emprestimo(models.Model):
    STATUS = [
        ('Em análise', 'Em análise'),
        ('Emprestado', 'Emprestado'),
        ('Finalizado', 'Finalizado'),
    ]

    data_emprestimo = models.DateField(auto_now_add=True, verbose_name="Data de Empréstimo")
    data_devolucao = models.DateField(null=True, blank=True, verbose_name="Data de Devolução")
    data_prevista_devolucao = models.DateTimeField(null=True, blank=True, verbose_name="Data Prevista de Devolução")
    status = models.CharField(max_length=50, choices=STATUS, verbose_name="Status")
    livro = models.ForeignKey('livros.Livro', on_delete=models.CASCADE, verbose_name="Livro")
    # usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, verbose_name="Usuário")

    def __str__(self):
        return f"{self.livro} - "
    
    def solicitar_emprestimo(self):
        self.status = 'Em análise'
        self.save()
    
    def save(self, *args, **kwargs):
        # if not self.livro.esta_disponivel():
        #     raise ValueError("Este livro não está disponível para empréstimo.")

        # Decrementa a quantidade disponível do livro ao salvar um novo emprestimo
        if self.pk is None:  
            self.livro.quantidade_disponivel -= 1
            self.data_prevista_devolucao = timezone.now() + timezone.timedelta(days=7)
            self.status = 'Em análise'
            self.livro.save()

        super().save(*args, **kwargs)

    def aprovar_emprestimo(self):
        self.status = 'Emprestado'
        self.data_prevista_devolucao = timezone.now() + timezone.timedelta(days=7)
        self.save()

    def registrar_devolucao(self):
        self.data_devolucao = timezone.now().date()
        self.status = 'Finalizado'
        self.livro.quantidade_disponivel += 1
        self.livro.save()
        self.save()


    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
        ordering = ['data_emprestimo']
