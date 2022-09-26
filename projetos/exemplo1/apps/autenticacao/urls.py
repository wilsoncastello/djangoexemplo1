from django.urls import path
from autenticacao import views

app_name = 'autenticacao'

urlpatterns = [
    path('',views.login_usuario,name='login_usuario'),
    path('autenticacao/novo-usuario/',views.add_usuario,name='add_usuario'),
    path('autenticacao/logout/',views.logout_usuario,name='logout_usuario'),
   ]