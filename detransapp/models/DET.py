from django.db import models
from detransapp.manager import DETManager

class Configuracao_DET(models.Model):
    tipo_registro = models.CharField(max_length=1)
    formato = models.CharField(max_length=6)
    cod_entidade = models.CharField(max_length=3)
    entidade = models.CharField(max_length=40)
    autuador = models.CharField(max_length=6)
    tipo_arquivo = models.CharField(max_length=1)
    filler = models.IntegerField()

    class Meta:
        app_label = "detransapp"


class DET(models.Model):
	codigo = models.CharField(max_length=255)

	objects = DETManager()

	class Meta:
		app_label = "detransapp"
