# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator

from detransapp.forms.especie import FormEspecie
from detransapp.forms.importacao import FormArquivo
from detransapp.models import Especie
from detransapp.serializers import EspecieSerializer
from detransapp.rest import JSONResponse
from detransapp.decorators import validar_imei


class CadastroEspecieView(View):
    template = 'especie/salvar.html'

    def get(self, request, especie_id=None):
        if especie_id:
            especie = Especie.objects.get(pk=especie_id)
            form = FormEspecie(instance=especie)
        else:
            form = FormEspecie()

        return render(request, self.template, {'form': form})

    def post(self, request, especie_id=None):

        if especie_id:
            especie = Especie.objects.get(pk=especie_id)
            form = FormEspecie(instance=especie, data=request.POST)
        else:
            form = FormEspecie(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

        return render(request, self.template, {'form': form})


class ConsultaEspecieView(View):
    template_name = 'especie/consulta.html'

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

        especies_page = Especie.objects.get_page(page, procurar)
        print especies_page
        return render(request, self.template_name, {'especies': especies_page, 'procurar': procurar})

    def get(self, request):

        return self.__page(request)

    def post(self, request):

        return self.__page(request)


class GetEspeciesRestView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    @method_decorator(validar_imei())
    def post(self, request):
        if 'data' in request.POST:
            especies = Especie.objects.get_especies_sicronismo(request.POST['data'])
        else:
            especies = Especie.objects.get_especies_sicronismo()

        especies_js = []
        for especie in especies:
            serializer = EspecieSerializer(especie)
            especies_js.append(serializer.data)
        return JSONResponse(especies_js)


class ImportaEspecie(View):
    template_name = 'especie/importa.html'

    def get(self, request):
        form = FormArquivo()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        i = 0
        arq = request.FILES['arquivo']
        for linha in arq:

            try:
                linha = linha.encode('UTF-8')
                cod = linha[0:2]
                desc = linha[2:].strip()
                novaEspecie = Especie(codigo=cod, descricao=desc)
                e = novaEspecie.save()
                i += 1
            except:
                continue

        return render(request, self.template_name, {'qtd': i, 'envio': True})
