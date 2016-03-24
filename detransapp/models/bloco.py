from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
=======
from agente import Agente
>>>>>>> 42530833b14b0f1113b8362e49e66e19662d0de8

from detransapp.manager import BlocoManager


<<<<<<< HEAD
=======

>>>>>>> 42530833b14b0f1113b8362e49e66e19662d0de8
class Bloco(models.Model):
    inicio_intervalo = models.IntegerField()
    fim_intervalo = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)
<<<<<<< HEAD
    ativo = models.BooleanField(default=True)
    contador = models.IntegerField(default=0)
=======
    agente_campo = models.ForeignKey(Agente, null=True, blank=True, related_name='+')
    ativo = models.BooleanField(default=True)
    
    
>>>>>>> 42530833b14b0f1113b8362e49e66e19662d0de8

    objects = BlocoManager()
