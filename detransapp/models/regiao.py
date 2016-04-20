from django.db import models

from detransapp.manager import RegiaoManager


class Regiao(models.Model):
    nome = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)
    objects = RegiaoManager()

    class Meta:
        app_label = "detransapp"
