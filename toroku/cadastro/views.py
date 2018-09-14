from django.shortcuts import render
from .models import *

# Create your views here.
def cadastro(request):
    visitante = Visitante.objects.all()
    return render(request, 'cadastro/visitante.html', {'visitante':visitante})
