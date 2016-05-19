# coding: utf-8
from datetime import datetime
import random

from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View

from detransapp.forms.DET import FormDet
from detransapp.models import Configuracao_DET, Infracao, DET
import os


class CadastroDETView(View):
    template = 'det/salvar.html'

    def get(self, request, det_id=None):

        if det_id:
            det = Configuracao_DET.objects.get(pk=det_id)
            form = FormDet(instance=det)
        else:
            form = FormDet()

        return render(request, self.template, {'form': form})

    def post(self, request, det_id=None):

        if det_id:
            cor = Configuracao_DET.objects.get(pk=det_id)
            form = FormDet(instance=cor, data=request.POST)
        else:

            form = FormDet(request.POST)

        if form.is_valid():
            form.save(request)

            return redirect('/')

        return render(request, self.template, {'form': form})


class ConsultaDETView(View):
    template_name = 'det/consulta.html'

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

        det_page = DET.DET.objects.get_page(page, procurar)

        return render(request, self.template_name, {'dets': det_page, 'procurar': procurar})

    def get(self, request):
        return self.__page(request)

    def post(self, request):
        return self.__page(request)


class TemplateDET(View):
    template_name = 'det/template.html'

    def get(self, request):
        return render(request, self.template_name, )


class GeraDet(View):
    template_name = 'det/gera.html'

    def get(self, request, filtro='0'):
        det = datetime.now().strftime("%Y%m%d%H%M%S")

        sequencial_arquivo = random.randrange(0, 999999)

        nome_arq = 'DET007.016.008088.' + str(sequencial_arquivo) + '.DET'
        arq = open(nome_arq, 'w')

        if filtro =='0':
            det_novo = DET.DET(codigo=det)
            det_novo.save()

        # topo
        config = Configuracao_DET.objects.get(id=1)

        hoje = datetime.now()

        filler_entidade = len(config.entidade)
        entidade = config.entidade
        if filler_entidade < 40:
            qtd = 40 - filler_entidade
            entidade = config.entidade + ' ' * qtd

        data = hoje.strftime('%d%m%Y')

        hora = hoje.strftime('%H%M')

        filler = config.filler * ' '

        sequencial_registro = 123456

        topo = config.tipo_registro + config.formato + config.cod_entidade + entidade + data + hora + str(
            sequencial_arquivo) + config.autuador + config.tipo_arquivo + filler + str(sequencial_registro)
        arq.write(topo + '\n')

        # infracoes
        infracoes = Infracao.objects.filter(det=filtro, veiculo_id__isnull=False).distinct()
        seq = 0
        
        for i in infracoes:
            seq += 1
            strseq = ('0' * (6 - len(str(seq)))) + str(seq)
            tipo_registro = '1'
            n_auto = str(i.id)
            if len(n_auto) < 10:
                n_auto = ('0' * (10 - len(n_auto))) + n_auto
            local = i.local
            if len(local) < 80:
                local = ' ' * (80 - len(local)) + local

            cod_municipio = '9999'

            
            cod_tipo_inf = str(i.tipo_infracao_id)

            if len(cod_tipo_inf) < 4:
                cod_tipo_inf = ('0' * (4 - len(cod_tipo_inf))) + cod_tipo_inf
            print(cod_tipo_inf)

            desmembramento = '1'

            condutor = '0'

            cnh = ' ' * 11

            complemento = 'c' * 80

            if i.is_condutor_identi:
                condutor = '1'
                cnh = i.infrator.cnh
                if len(cnh) < 11:
                    cnh = cnh + ' ' * (11 - len(cnh))

            filler = ' ' * 31

        

            infracao = tipo_registro + n_auto + i.veiculo.placa + i.veiculo.cidade.uf.sigla + i.data_infracao.strftime(
                '%d%m%Y') + i.data_infracao.strftime(
                '%H%M%S') + local + cod_municipio + cod_tipo_inf + desmembramento + condutor + cnh + i.agente.cpf + complemento + filler + str(
                strseq)
            print(len(infracao))
            infracao = infracao.encode('UTF-8')
            arq.write(infracao + '\n')
            if i.det =='0':
                i.det = det
                i.save()

        # trailer
        qtd = len(infracoes)

        if len(str(qtd)) < 6:
            qtd = ('0' * (6 - qtd)) + str(qtd)
        trailer = '9' + str(qtd) + ' ' * 250 + str(sequencial_registro)
        arq.write(trailer + '\n')
        print(arq)

        arq.close()
        down = open(nome_arq, 'r')
        response = HttpResponse(down, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % nome_arq
        os.remove(nome_arq)
        return response
