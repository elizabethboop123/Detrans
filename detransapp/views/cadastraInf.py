import random

from django.shortcuts import redirect
from django.utils import timezone

from detransapp.models import *


# tipo_veiculo = models.ForeignKey(TipoInfracao)
# condutor = models.ForeignKey(Condutor)
# agente = models.ForeignKey(Agente)
# veiculo = models.ForeignKey(Veiculo)
# tempo = models.DateTimeField()
# obs = models.TextField()
# id_sincronia = models.CharField(max_length=60, unique=True)
# movimento = models.ForeignKey(Movimentacao)
# data_infracao = models.DateTimeField()
# data_sincronizacao = models.DateTimeField(auto_now=True)
def cad(request):
    tipo = TipoInfracao.objects.all()[0]
    condutor = Condutor.objects.all()[0]
    agente = Agente.objects.all()[0]
    veiculo = Veiculo.objects.all()[0]
    m = Movimentacao(tempo=timezone.now(), latitude=1.56, longitude=1.32)
    m.save()
    n = random.randint(0, 100000000000000000000000000000000)
    inf = Infracao(tipo=tipo, condutor=condutor, agente=agente, veiculo=veiculo, id_sincronia=n, tempo=timezone.now(),
                   movimento=m, data_infracao=timezone.now())
    inf.save()
    print(veiculo)
    return redirect('/')
