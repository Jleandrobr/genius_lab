from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from .models import UserProfile
from rolepermissions.roles import assign_role

class CustomUserCreationForm(UserCreationForm):
    endereco = forms.CharField(max_length=255, required=False, label='Endereço')
    telefone = forms.CharField(max_length=20, required=False, label='Telefone')
    grupo = forms.ChoiceField(choices=[('Administrador', 'Administrador'), ('Leitor', 'Leitor')])

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            group_name = self.cleaned_data['grupo']
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            
            
            if group_name == 'Administrador':
                user.is_superuser = True
                user.is_staff = True
                
                admin_permissions = Permission.objects.all()  
                user.user_permissions.set(admin_permissions)
            
            
            elif group_name == 'Leitor':
                reader_permissions = Permission.objects.filter(
                    codename__in=['add_emprestimo', 'view_emprestimo', 'view_livro']
                )
                user.user_permissions.set(reader_permissions)

            user.save()  
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'
