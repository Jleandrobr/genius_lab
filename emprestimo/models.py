from django.db import models
from livros.models import Livro
from django.utils import timezone

# Create your models here.

class Emprestimo(models.Model):
    STATUS = [
        ('Aberto', 'Aberto'),
        ('Concluído', 'Concluído'),
    ]

    data_emprestimo = models.DateField(auto_now_add=True, verbose_name="Data de Empréstimo")
    data_devolucao = models.DateField(null=True, blank=True, verbose_name="Data de Devolução")
    data_prevista_devolucao = models.DateTimeField(verbose_name="Data Prevista de Devolução")
    status = models.CharField(max_length=50, choices=STATUS, verbose_name="Status")
    livro = models.ForeignKey('livros.Livro', on_delete=models.CASCADE, verbose_name="Livro")
    # usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, verbose_name="Usuário")

    def __str__(self):
        return f"{self.livro} - "
    
    def save(self, *args, **kwargs):
        if not self.livro.esta_disponivel():
            raise ValueError("Este livro não está disponível para empréstimo.")

        # Decrementa a quantidade disponível do livro ao salvar um novo emprestimo
        if self.pk is None:  
            self.livro.quantidade_disponivel -= 1
            self.livro.save()

        super().save(*args, **kwargs)

    def registrar_devolucao(self):
        self.data_devolucao = timezone.now().date()
        self.status = 'Concluído'
        self.livro.quantidade_disponivel += 1
        self.livro.save()
        self.save()


    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
        ordering = ['data_emprestimo']
