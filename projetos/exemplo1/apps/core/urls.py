from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('home', views.home,name='home'),
    path('categoria/adicionar/',views.add_categoria,name='add_categoria'),
    path('categoria/listar/',views.lista_categorias,name='lista_categorias'),
    path('categoria/editar/<int:id_categoria>/',views.edita_categoria,name='edita_categoria'),
    path('categoria/excluir/<int:id_categoria>/',views.exclui_categoria,name='exclui_categoria'),
    path('compromisso/adicionar/',views.add_compromisso,name='add_compromisso'),
    path('compromisso/listar/',views.lista_compromissos,name='lista_compromissos'),
    path('compromisso/editar/<int:id_compromisso>/',views.edita_compromisso,name='edita_compromisso'),
    path('compromisso/excluir/<int:id_compromisso>/',views.exclui_compromisso,name='exclui_compromisso'),
]
