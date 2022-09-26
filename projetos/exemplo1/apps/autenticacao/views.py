from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required

def add_usuario(request):
    template_name = 'autenticacao/add_usuario.html'
    context = {}
    if request.method =='POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            return redirect('autenticacao:login_usuario')
    form = UsuarioForm()
    context['form'] = form
    return render(request, template_name , context)

def login_usuario(request):
    template_name = 'autenticacao/login_usuario.html'
    context = {}
    if request.method =='POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario,password=senha)
        if user is not None:
            login(request, user)
            return redirect('core:home')
    return render(request, template_name , context)

@login_required(login_url='/')
def logout_usuario(request):
    logout(request)
    return redirect('autenticacao:login_usuario')