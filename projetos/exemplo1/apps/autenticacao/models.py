from django.db import models
from django.contrib.auth.models import User

class Usuario (User, models.Model):
    telefone = models.CharField('Telefone',max_length=16)

    def __str__(self):
        return self.user.username
