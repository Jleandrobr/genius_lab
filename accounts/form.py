from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    endereco = forms.CharField(max_length=255, required=False, label='Endereço')
    telefone = forms.CharField(max_length=20, required=False, label='Telefone')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'groups','password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                endereco=self.cleaned_data.get('endereco'),
                telefone=self.cleaned_data.get('telefone')
            )
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'
