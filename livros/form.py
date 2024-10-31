from django.forms import ModelForm
from .models import Livro


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
        exclude = ['isbn']  