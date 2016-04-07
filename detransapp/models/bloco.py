from django.db import models
from django.contrib.auth.models import User
from agente import Agente

from detransapp.manager import BlocoManager



class Bloco(models.Model):
    inicio_intervalo = models.IntegerField()
    fim_intervalo = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)
    agente_campo = models.ForeignKey(Agente, null=True, blank=True, related_name='+')
    ativo = models.BooleanField(default=True)
    minimo_pag_restantes = models.IntegerField(null=True)
    
    

    objects = BlocoManager()
