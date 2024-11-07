from django.shortcuts import render, redirect
# from .admin import CustomUserCreationForm
from django.contrib import messages
from .form import CustomUserCreationForm

def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.is_valid = False
            user.save()
            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('login')
        
            
    return render(request, "registration/register.html",{"form": form})