# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.generic.base import View
from django.utils.decorators import method_decorator

from detransapp.models import Cidade, UF
from detransapp.serializers import CidadeSerializer
from detransapp.rest import JSONResponse
from detransapp.decorators import validar_imei
from detransapp.forms.importacao import FormArquivo


@csrf_exempt
def get_cidades(request):
    cidades = Cidade.objects.filter(uf_id=request.POST['uf']).order_by('nome')
    cidades_json = serializers.serialize('json', cidades)
    return HttpResponse(cidades_json)


class GetCidadesRestView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    @method_decorator(validar_imei())
    def post(self, request):
        if 'data' in request.POST:
            cidades = Cidade.objects.get_cidades_sicronismo(int(request.POST['uf_id']), request.POST['data'])
        else:
            cidades = Cidade.objects.get_cidades_sicronismo(int(request.POST['uf_id']))
        json_cidades = []
        for uf in cidades:
            serializer = CidadeSerializer(uf)
            json_cidades.append(serializer.data)

        return JSONResponse(json_cidades)


class ImportaCidade(View):
    template_name = 'cidade/importa.html'

    def get(self, request):
        form = FormArquivo()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        arq = request.FILES['arquivo']
        i = 0
        uf = UF.objects.filter(sigla='SC').first()

        if uf is None:
            uf = UF(sigla='SC', nome='Santa Catarina')
            uf.save()

        for linha in arq:
            try:
                linha = linha.encode('UTF-8')
                cod = int(linha[:4])
                cidade = linha[4:44].strip()
                novaCidade = Cidade(uf_id=uf.id, codigo=cod, nome=cidade)
                novaCidade.save()
                i += 1
            except:
                continue

        return render(request, self.template_name, {'qtd': i, 'envio': True})
