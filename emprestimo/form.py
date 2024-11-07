from django.forms import ModelForm
from .models import Emprestimo


class EmprestimoForm(ModelForm):

    class Meta:
        model = Emprestimo
        fields = '__all__'
        exclude = ['data_emprestimo', 'data_devolucao', 'data_prevista_devolucao', 'status']