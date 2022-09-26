from django.shortcuts import render, redirect
from core.forms import CategoriaForm, CompromissoForm
from .models import Categoria, Compromisso
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/')
def home(request):
    return render(request, 'base.html', {})

@login_required(login_url='/')
def add_categoria(request):
    template_name = 'core/add_categoria.html'
    context = {}
    if request.method =='POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    form = CategoriaForm()
    context['form'] = form
    return render(request, template_name , context)

@login_required(login_url='/')
def lista_categorias(request):
    template_name = 'core/lista_categorias.html'
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, template_name, context)

@login_required(login_url='/')
def edita_categoria(request, id_categoria):
    template_name = 'core/add_categoria.html'  
    context = {}
    categoria = Categoria.objects.get(id=id_categoria)
    if request.method =='POST':
        form = CategoriaForm(request.POST,instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('core:lista_categorias')
    form = CategoriaForm(instance=categoria)
    context['form'] = form
    return render(request, template_name , context)

@login_required(login_url='/')
def exclui_categoria(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    categoria.delete()
    return redirect('core:lista_categorias')

@login_required(login_url='/')
def add_compromisso(request):
    template_name = 'core/add_compromisso.html'
    context = {}
    if request.method =='POST':
        form = CompromissoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.pessoa = request.user
            f.save()
            form.save_m2m()
    form = CompromissoForm()
    context['form'] = form
    return render(request, template_name , context)

@login_required(login_url='/')
def lista_compromissos(request):
    template_name = 'core/lista_compromissos.html'
    compromissos = Compromisso.objects.filter(pessoa=request.user)
    context = {
        'compromissos': compromissos
    }
    return render(request, template_name, context)

@login_required(login_url='/')
def edita_compromisso(request, id_compromisso):
    template_name = 'core/add_compromisso.html'  
    context = {}
    compromisso = Compromisso.objects.get(id=id_compromisso)
    if request.method =='POST':
        form = CompromissoForm(request.POST,instance=compromisso)
        if form.is_valid():
            form.save()
            return redirect('core:lista_compromissos')
    form = CompromissoForm(instance=compromisso)
    context['form'] = form
    return render(request, template_name , context)

@login_required(login_url='/')
def exclui_compromisso(request, id_compromisso):
    compromisso = Compromisso.objects.get(id=id_compromisso)
    compromisso.delete()
    return redirect('core:lista_compromissos')