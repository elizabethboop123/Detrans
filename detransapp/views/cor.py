# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated, AllowAny

from detransapp.forms.cor import FormCor
from detransapp.forms.importacao import FormArquivo
from detransapp.models import Cor
from detransapp.decorators import validar_imei
from detransapp.rest import JSONResponse
from detransapp.serializers import CorSerializer


class CadastroCorView(View):
    template = 'cor/salvar.html'

    def get(self, request, cor_id=None):

        if cor_id:
            cor = Cor.objects.get(pk=cor_id)
            form = FormCor(instance=cor)
        else:
            form = FormCor()

        return render(request, self.template, {'form': form})

    def post(self, request, cor_id=None):

        cor_id = request.POST['codigo']
        if cor_id:
            cor = Cor.objects.get(pk=cor_id)
            form = FormCor(instance=cor, data=request.POST)
        else:

            form = FormCor(request.POST)

        if form.is_valid():
            form.save(request)

            return redirect('/')

        return render(request, self.template, {'form': form})


class ConsultaCorView(View):
    template_name = 'cor/consulta.html'

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

        cores_page = Cor.objects.get_page(page, procurar)

        return render(request, self.template_name, {'cores': cores_page, 'procurar': procurar})

    def get(self, request):
        return self.__page(request)

    def post(self, request):
        return self.__page(request)


class GetCoresRestView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    @method_decorator(validar_imei())
    def post(self, request):
        if 'data' in request.POST:
            cores = Cor.objects.get_cores_sicronismo(request.POST['data'])
        else:
            cores = Cor.objects.get_cores_sicronismo()

        cores_js = []
        for cor in cores:
            serializer = CorSerializer(cor)
            cores_js.append(serializer.data)
        return JSONResponse(cores_js)


class ImportaCor(View):
    template_name = 'cor/importa.html'

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
                cor = linha[2:].strip()
                novaCor = Cor.objects.filter(codigo=cod).first()

                if novaCor:
                    novaCor.descricao = cor
                else:
                    novaCor = Cor(codigo=cod, descricao=cor)

                novaCor.save()
                print(i)
                i += 1
            except:
                pass

        return render(request, self.template_name, {'qtd': i, 'envio': True})
