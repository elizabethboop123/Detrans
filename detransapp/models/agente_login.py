from django.db import models
from agente import Agente
from dispositivo import Dispositivo


class Agente_login(models.Model):

    device = models.ForeignKey(Dispositivo)
    agente = models.ForeignKey(Agente)
    status = models.BooleanField(default=False)
    data_login = models.DateTimeField(auto_now_add=True) 
    data_logout = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    class Meta:
        app_label = "detransapp"