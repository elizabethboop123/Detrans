from django.db import models
from django.contrib.auth.models import User

from detransapp.manager import AgenteManager
from detransapp.models.movimentacao import Movimentacao
from detransapp.models.regiao import Regiao


class Agente(User):
    identificacao = models.CharField(max_length=6)
    movimentos = models.ManyToManyField(Movimentacao)
    regioes = models.ManyToManyField(Regiao)
    data = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)
<<<<<<< HEAD

    objects = AgenteManager()

    class Meta:
        app_label = "detransapp"
=======
    cpf = models.CharField(max_length=11, default='12345678901')

    objects = AgenteManager()

    def __unicode__(self):
        return self.identificacao

    class Meta:
        app_label = "detransapp"
>>>>>>> 42530833b14b0f1113b8362e49e66e19662d0de8
