# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator

from detransapp.forms.tipo_veiculo import FormTipoVeiculo
from detransapp.models import TipoVeiculo
from detransapp.forms.importacao import FormArquivo
from detransapp.serializers import TipoVeiculoSerializer
from detransapp.rest import JSONResponse
from detransapp.decorators import validar_imei


class CadastroTipoView(View):
    template = 'tipo_veiculo/salvar.html'

    def get(self, request, tipo_id=None):

        if tipo_id:
            tipo = TipoVeiculo.objects.get(pk=tipo_id)
            form = FormTipoVeiculo(instance=tipo)
        else:
            form = FormTipoVeiculo()

        return render(request, self.template, {'form': form})

    def post(self, request, tipo_id=None):

        tipo_id = request.POST['codigo']

        if tipo_id:
            tipo = TipoVeiculo.objects.get(pk=tipo_id)
            form = FormTipoVeiculo(instance=tipo, data=request.POST)
        else:

            form = FormTipoVeiculo(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

        return render(request, self.template, {'form': form})


class ConsultaTipoView(View):
    template_name = 'tipo_veiculo/consulta.html'

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

        tipos_page = TipoVeiculo.objects.get_page(page, procurar)

        return render(request, self.template_name, {'tipos': tipos_page, 'procurar': procurar})

    def get(self, request):

        return self.__page(request)

    def post(self, request):

        return self.__page(request)


class GetTiposVeiculoRestView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    @method_decorator(validar_imei())
    def post(self, request):
        if 'data' in request.POST:
            tipos = TipoVeiculo.objects.get_tipos_veiculo_sicronismo(request.POST['data'])
        else:
            tipos = TipoVeiculo.objects.get_tipos_veiculo_sicronismo()
        tipos_js = []
        for veiculo in tipos:
            serializer = TipoVeiculoSerializer(veiculo)
            tipos_js.append(serializer.data)
        return JSONResponse(tipos_js)


class ImportaTipoVeiculo(View):
    template_name = 'tipo_veiculo/importa.html'

    def get(self, request):
        form = FormArquivo()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        arq = request.FILES['arquivo']
        i = 0
        for linha in arq:
            try:
                linha = linha.encode('UTF-8')
                cod = linha[0:2]
                desc = linha[2:].strip()
                novaCategoria = TipoVeiculo(codigo=cod, descricao=desc)
                novaCategoria.save()
                i += 1
            except:
                pass

        return render(request, self.template_name, {'qtd': i, 'envio': True})
