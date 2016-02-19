from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.db.models import Count

from detransapp.views.modelo import CadastroModeloView, ConsultaModeloView, GetModelosRestView, ImportaModelo
from detransapp.views.tipo_veiculo import CadastroTipoView, ConsultaTipoView, GetTiposVeiculoRestView, \
    ImportaTipoVeiculo
from detransapp.views.tipo_infracao import CadastroTipoInfracaoView, ConsultaTipoInfracaoView, GetTiposInfracaoRestView, \
    CarregaTiposInfracao
from detransapp.views.especie import CadastroEspecieView, ConsultaEspecieView, GetEspeciesRestView, ImportaEspecie
from detransapp.views.agente import CadastroAgenteView, ConsultaAgenteView, GetAgentesRestView
from detransapp.views.veiculo import CadastroVeiculoView, ConsultaVeiculoView, GetVeiculosRestView, ImportaVeiculo
from detransapp.views.condutor import CadastroCondutorView, ConsultaCondutorView
from detransapp.views.proprietario import CadastroProprietarioView, ConsultaProprietarioView
from detransapp.views.dispositivo import CadastroDispositivoView, ConsultaDispositivoView
from detransapp.views.infracao import RelatorioInfracaoView, RecebeInfracoesRestView
from detransapp.views.modelo import GetModelosRestView
from detransapp.views.regiao import GetRegioesRestView
from detransapp.views.uf import GetUFsRestView
from detransapp.views.cidade import GetCidadesRestView, ImportaCidade
from detransapp.views.sincronismo import SincronismoRestView
from detransapp.views.leis import CadastroLeisView, ConsultaLeisView
from detransapp.views.bloco import CadastroBlocoView, ConsultaBlocoView, GetBlocoRestView
from detransapp.views.cor import CadastroCorView, ConsultaCorView, ImportaCor, GetCoresRestView
from detransapp.views.categoria import CadastroCategoriaView, ConsultaCategoriaView, ImportaCategoria, \
    GetCategoriasRestView
from detransapp.views.tipo_cancelamento import CadastroCancelamentoView, ConsultaCancelamentoView
from detransapp.views.download_detrans import DownloadDetransView, DownloadDetransApkView
from detransapp.views.config_sinc import GetConfigSincRestView
from detransapp.views.detrans_arquivo_sqlite import CriaSqliteView, StatusView
# from detransapp.views.DET import *
import detransapp.views.cadastraInf
from detransapp.models import *


def naoSinc():
    startdate = timezone.now() - timedelta(days=1)
    enddate = timezone.now()
    agts = Agente.objects.all()
    td = Infracao.objects.filter(data_infracao__range=[startdate, enddate])
    sinc = []
    ns = []
    for i in td:
        sinc.append(i.agente)
    for a in agts:
        if a not in sinc:
            ultima = Infracao.objects.filter(agente_id=a.id)
            if ultima:
                ultima = ultima[0]
                print('aqui')
                print(ultima.data_sincronizacao)
                ns.append({'agente': a, 'tempo': ultima.data_sincronizacao})
            else:
                ns.append({'agente': a})

    if len(ns) >= 5:
        ns = ns[:5]
    return ns


def graficoInfracoes():
    horas = {"data": """strftime('%H', data_infracao)"""}
    d = Infracao.objects.extra(select=horas).values('data').annotate(Count('data_infracao')).order_by('-data')
    # print d
    # #Step 1: Create a DataPool with the data we want to retrieve.
    # dados = DataPool(series=
    #		 [{'options': {
    #			'source': d},
    #		   'terms': [
    #			 'data',
    #			 'data_infracao__count']}
    #		 ])

    # #Step 2: Create the Chart object
    # cht = Chart(
    #		 datasource = dados,
    #		 series_options =
    #		   [{'options':{
    #			   'type': 'line',
    #			   'stacking': False},
    #			 'terms':{
    #			   'data': [
    #				 'data_infracao__count']
    #			   }}],
    #		 chart_options =
    #		   {'title': {
    #				'text': 'Weather Data of Boston and Houston'},
    #			'xAxis': {
    #				 'title': {
    #					'text': 'Month number'}}})

    # #Step 3: Send the chart object to the template.
    return d


def ultimasSinc():
    return Infracao.objects.order_by('-data_infracao')[:5]


def grafico1():
    return


def ultimaHora():
    startdate = timezone.now() - timedelta(hours=1)
    enddate = timezone.now()
    return Infracao.objects.filter(data_infracao__range=[startdate, enddate]).annotate(Count('agente')).order_by(
        'data_infracao')[:5]


def diario():
    return None
    weekday = {"data": """strftime('%d/%m/%Y', data_infracao)"""}
    d = Infracao.objects.extra(select=weekday).values('data').annotate(Count('data_infracao')).order_by('-data')
    if len(d) >= 5:
        return d[0:5]
    else:
        return d


@login_required
def index(request):
    return render_to_response("index.html", RequestContext(request, {'ultimasSinc': ultimasSinc(), 'naoSinc': naoSinc(),
                                                                     'diario': diario(), 'ultimaHora': ultimaHora(),
                                                                     'graficoInfracoes': graficoInfracoes()}))


@login_required
def relatorios(request):
    return render_to_response('relatorios.html', RequestContext(request))


def about(request):
    return render_to_response("sobre.html", RequestContext(request))
