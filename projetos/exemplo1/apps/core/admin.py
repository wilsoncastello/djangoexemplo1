from django.contrib import admin

from .models import Categoria
from .models import Compromisso
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Compromisso)

admin.site.unregister(Group)
admin.site.site_header = 'Agenda de Compromissos'
admin.site.index_title = 'Agenda de Compromissos - Aplicações'


