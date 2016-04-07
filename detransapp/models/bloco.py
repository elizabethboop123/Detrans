from django.db import models
from django.contrib.auth.models import User

from detransapp.manager import BlocoManager


class Bloco(models.Model):
    inicio_intervalo = models.IntegerField()
    fim_intervalo = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)
    ativo = models.BooleanField(default=True)
<<<<<<< HEAD
    minimo_pag_restantes = models.IntegerField(null=True)
    
    
=======
    contador = models.IntegerField(default=0)
>>>>>>> 1a7e28163ca8c15961f8c29385178cfd18e9c58f

    objects = BlocoManager()
