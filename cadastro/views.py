from django.shortcuts import render
from .models import *
from .forms import VisitanteForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cadastro(request):
    if request.method == "POST":
        form = VisitanteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'cadastro/sucesso.html', {'form': form})
    else:
        form = VisitanteForm()

    return render(request, 'cadastro/visitante.html', {'form': form})

def home(request):
    return render(request, 'cadastro/home.html')
