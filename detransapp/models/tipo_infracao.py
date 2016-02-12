from django.db import models

from detransapp.manager import TipoInfracaoManager
from lei import Lei


class TipoInfracao(models.Model):
    codigo = models.CharField(primary_key=True, max_length=20)
    descricao = models.CharField(max_length=200)
    lei = models.ForeignKey(Lei)
    is_condutor_obrigatorio = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    objects = TipoInfracaoManager()

    def __unicode__(self):
        return self.descricao

    class Meta:
        app_label = "detransapp"
