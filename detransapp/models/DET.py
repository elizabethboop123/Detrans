from django.db import models


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
