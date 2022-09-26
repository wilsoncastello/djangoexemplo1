from django import forms
from .models import Categoria, Compromisso

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('nome', 'descricao')


class CompromissoForm(forms.ModelForm):

    class Meta:
        model = Compromisso
# Versão 1.0 usada na aula 6 com todos os campos.
#       fields = ('titulo', 'descricao', 'data', 'hora', 'prioridade', 'status', 'categoria','pessoa')
#       exclude = ()

 # Versão 2.0 usada na aula 7 sem o campo pessoa.
 #      fields = ('titulo', 'descricao', 'data', 'hora', 'prioridade', 'status', 'categoria')
        exclude = ('pessoa', )

