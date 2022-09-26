from dataclasses import dataclass
from telnetlib import STATUS
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField('Nome',max_length=150)
    descricao = models.TextField('Descrição', blank=True, null=True)

    def __str__(self):
        return self.nome
    

class Compromisso(models.Model):
    OPCOES_PRIORIDADES = (
        ('B','Baixa'),
        ('M','Média'),
        ('A','Alta'),
    )

    OPCOES_STATUS = (
        ('RD','Realizado'),
        ('CL','Cancelado'),
        ('AD','Adiado'),
        ('AG','Agendado'),
    )

    titulo = models.CharField('Título', max_length=200)
    descricao = models.TextField('Descrição',blank=True, null=True)
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    hora = models.TimeField('Hora', auto_now=False, auto_now_add=False)
    prioridade = models.CharField('Prioridade', max_length=1, choices=OPCOES_PRIORIDADES)
    status = models.CharField('Status', max_length=2, choices=OPCOES_STATUS)
    categoria = models.ManyToManyField(Categoria)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo