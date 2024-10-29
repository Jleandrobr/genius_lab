from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
# from .models import Livro

def home(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'livros/home.html')

# def home(request):
#     livros = Livro.objects.all()
#     template = loader.get_template('home.html')
#     context = {
#         'livros': livros
#     }
#     return HttpResponse(template.render(context, request))

# Create your views here.
