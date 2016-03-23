from django.db import models


class MedidaAdminstrativa(models.Model):
    codigo = models.CharField(max_length=10)
    descricao = models.TextField(null=True)
