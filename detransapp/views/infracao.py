# coding: utf-8
# from wkhtmltopdf.views import PDFTemplateResponse
# from pandas.tseries.frequencies import infer_freq
from json import loads, dumps
from datetime import datetime

from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from django.db import transaction
from django.utils.decorators import method_decorator

from detransapp.models import Infracao
from detransapp.models import Infrator, Movimentacao, Dispositivo, VeiculoEditado, VeiculoEstrangeiro
from detransapp.decorators import validar_imei


class RelatorioInfracaoView(View):
    template = 'infracao/relatorio.html'

    # def get(self, request):
    #	 '''response = PDFTemplateResponse(request=request,
    #									template=self.template,
    #									filename="relatorio_infracao.pdf",
    #									context=self.context,
    #									show_content_in_browser=True,
    #									cmd_options={'margin-top': 15,},
    #									)
    #	 return response'''
    #	 return None

    def __page(self, request):
        procurar = ''

        if request.method == 'POST':

            if 'procurar' in request.POST:
                procurar = request.POST['procurar']

        else:

            if 'procurar' in request.GET:
                procurar = request.GET['procurar']

        try:
            page = int(request.GET.get('page', 1))
        except Exception:
            page = 1

        infracao_page = Infracao.objects.get_page(page, procurar)

        return render(request, self.template, {'infracoes': infracao_page, 'procurar': procurar})

    def get(self, request):

        return self.__page(request)

    def post(self, request):

        return self.__page(request)


class RecebeInfracoesRestView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    @method_decorator(validar_imei())
    # @method_decorator(transaction.atomic)
    def post(self, request):
        print request.POST['infracoes']
        infracoes_sinc = []
        infracoes_json = loads(request.POST['infracoes'])

        for inf_json in infracoes_json:
            sid = transaction.savepoint()
            try:
                is_estrangeiro = True
                if inf_json['is_estrangeiro'] == '0':
                    is_estrangeiro = False

                is_editado = True

                if inf_json['is_editado'] == '0':
                    is_editado = False

                is_condutor_identificado = True

                if inf_json['is_condutor_identificado'] == '0':
                    is_condutor_identificado = False

                infracao = Infracao()
                infracao.agente_id = request.user.id
                # TODO REVISAR TABELA DISPOSITIVO CAMPO CHAVE IMEI
                infracao.dispositivo_id = Dispositivo.objects.get(imei=request.POST['imei']).id

                infracao.id = int(inf_json['infracao_id'])
                infracao.data_infracao = datetime.strptime(inf_json['data'], "%d/%m/%Y %H:%M:%S")
                infracao.local = inf_json['local']
                infracao.local_numero = inf_json['local_numero']

                infracao.veiculo_id = inf_json['veiculo_id']
                print 'inf_json[tipo_infracao_id] : ', inf_json['tipo_infracao_id']
                infracao.tipo_infracao_id = inf_json['tipo_infracao_id']

                movimentacao = Movimentacao()
                movimentacao.tempo = datetime.strptime(inf_json['data'], "%d/%m/%Y %H:%M:%S")
                movimentacao.latitude = inf_json['latitude']
                movimentacao.longitude = inf_json['longitude']
                movimentacao.save()

                infracao.movimento_id = movimentacao.id

                if is_condutor_identificado:
                    infrator = Infrator()
                    infrator.nome = inf_json['infrator']['nome']
                    infrator.cnh = inf_json['infrator']['cnh']
                    infrator.documento = inf_json['infrator']['documento']
                    infrator.save()

                    infracao.infrator_id = infrator.documento

                infracao.is_estrangeiro = is_estrangeiro
                infracao.is_condutor_identi = is_condutor_identificado
                infracao.is_veiculo_editado = is_editado

                # TODO TA FALTANDO CAMPO BANCO DE DADOS
                '''try:
                    infracao.data_cancelamento = datetime.strptime( inf_json['data_cancelamento'],"%d/%m/%Y %H:%M:%S")
                    infracao.
                except:'''

                infracao.save(force_insert=True)

                if is_editado:
                    veiculo_editado = VeiculoEditado()
                    veiculo_editado.veiculo_id = inf_json['veiculo_id']
                    veiculo_editado.placa = inf_json['veiculo']['placa']

                    veiculo_editado.especie = inf_json['veiculo']['especie']
                    veiculo_editado.tipo_veiculo = inf_json['veiculo']['tipo_veiculo']
                    veiculo_editado.modelo = inf_json['veiculo']['modelo']
                    veiculo_editado.cor = inf_json['veiculo']['cor']
                    veiculo_editado.cidade = inf_json['veiculo']['cidade']
                    veiculo_editado.categoria = inf_json['veiculo']['categoria']
                    veiculo_editado.num_passageiro = inf_json['veiculo']['num_passageiros']

                    veiculo_editado.infracao_id = infracao.id
                    veiculo_editado.save()

                if is_estrangeiro:
                    veiculo_estrangeiro = VeiculoEstrangeiro()
                    veiculo_estrangeiro.pais = inf_json['veiculo']['pais']
                    veiculo_estrangeiro.modelo = inf_json['veiculo']['modelo']
                    veiculo_estrangeiro.especie = inf_json['veiculo']['especie']
                    veiculo_estrangeiro.placa = inf_json['veiculo']['placa']
                    veiculo_estrangeiro.chassi = inf_json['veiculo']['chassi']
                    veiculo_estrangeiro.nr_motor = inf_json['veiculo']['nr_motor']

                    veiculo_estrangeiro.ano_fabricacao = inf_json['veiculo']['ano_fabricacao']
                    veiculo_estrangeiro.ano_modelo = inf_json['veiculo']['ano_modelo']
                    veiculo_estrangeiro.num_passageiro = inf_json['veiculo']['num_passageiros']
                    veiculo_estrangeiro.infracao_id = infracao.id
                    veiculo_estrangeiro.save()

                    # TODO VERIFICAR SE ESSES CAMPOS ESTÃO CORRETOS
                    '''
                    veiculo_estrangeiro.tipo_veiculo_id = inf_json['veiculo']['tipo_veiculo_id']
                    veiculo_estrangeiro.cor_id = inf_json['veiculo']['cor_id']
                    veiculo_estrangeiro.categoria_id = inf_json['veiculo']['categoria_id']
                    '''
                infracoes_sinc.append({'id': infracao.id, 'status': True})
                transaction.savepoint_commit(sid)
            except:
                infracoes_sinc.append({'id': int(inf_json['infracao_id']), 'status': False})
                transaction.savepoint_rollback(sid)
        print infracoes_sinc
        json = dumps(infracoes_sinc, ensure_ascii=False)
        return HttpResponse(json)


class DET007(View):
    def gerar(self):
        infracoes = Infracao.objects.all()
        # cabecalho do file
        tipo_registro = 0
        formato = "DET007"
        cod_entidade = 016
        nome_entidade = "Detrans                                 "
        data = datetime.now()
        hoje = datetime.strftime('%d%m%Y')
        agora = datetime.strftime('%H%M')
        seq = '000001'
        cod_autuador = '008088'
        tipo = 'P'
        filler = ' '*182
        seq_file = '000001'


        for i in infracoes:
            return i

