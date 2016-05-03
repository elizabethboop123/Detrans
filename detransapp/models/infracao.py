from django.db import models

from detransapp.models.tipo_infracao import TipoInfracao
from detransapp.models.infrator import Infrator
from detransapp.models.agente import Agente
from detransapp.models.veiculo import Veiculo
from detransapp.models.movimentacao import Movimentacao
from detransapp.models.tipo_cancelamento import TipoCancelamento
from detransapp.models.dispositivo import Dispositivo
from detransapp.manager import InfracaoManager


class Infracao(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_infracao = models.ForeignKey(TipoInfracao, null=True)
    infrator = models.ForeignKey(Infrator, null=True)
    agente = models.ForeignKey(Agente, null=True)
    veiculo = models.ForeignKey(Veiculo, null=True)
    obs = models.TextField(null=True, blank=True)
    movimento = models.ForeignKey(Movimentacao, null=True)

    is_estrangeiro = models.BooleanField()
    is_veiculo_editado = models.BooleanField()

    is_condutor_identi = models.BooleanField()

    tipo_cancelamento = models.ForeignKey(TipoCancelamento, null=True, blank=True)
    justificativa = models.TextField(null=True, blank=True)
    dispositivo = models.ForeignKey(Dispositivo, null=True)

    local = models.CharField(max_length=255, null=True)
    local_numero = models.CharField(max_length=100, null=True)

    data_infracao = models.DateTimeField()
    data_sincronizacao = models.DateTimeField(auto_now=True)

    det = models.CharField(max_length=255, default='0')

    objects = InfracaoManager()

    class Meta:
        app_label = "detransapp"
