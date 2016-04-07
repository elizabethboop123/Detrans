# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated, AllowAny

from detransapp.forms.categoria import FormCategoria
from detransapp.models import Categoria
from detransapp.forms.importacao import FormArquivo
from detransapp.decorators import validar_imei
from detransapp.rest import JSONResponse
from detransapp.serializers import CategoriaSerializer


class CadastroCategoriaView(View):
    template = 'categoria/salvar.html'

    def get(self, request, categoria_id=None):

        if categoria_id:
            categoria = Categoria.objects.get(pk=categoria_id)
            form = FormCategoria(instance=categoria)
        else:
            form = FormCategoria()

        return render(request, self.template, {'form': form})

    def post(self, request, categoria_id=None):

        if categoria_id:
            categoria = Categoria.objects.get(pk=categoria_id)
            form = FormCategoria(instance=categoria, data=request.POST)
        else:

            form = FormCategoria(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

        return render(request, self.template, {'form': form})


class ConsultaCategoriaView(View):
    template_name = 'categoria/consulta.html'

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

        categorias_page = Categoria.objects.get_page(page, procurar)

        return render(request, self.template_name, {'categorias': categorias_page, 'procurar': procurar})

    def get(self, request):

        return self.__page(request)

    def post(self, request):

        return self.__page(request)


class GetCategoriasRestView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    # @method_decorator(validar_imei())
    def post(self, request):
        if 'data' in request.POST:
            categorias = Categoria.objects.get_categorias_sicronismo(request.POST['data'])
        else:
            categorias = Categoria.objects.get_categorias_sicronismo()

        cores_js = []
        for categoria in categorias:
            serializer = CategoriaSerializer(categoria)
            cores_js.append(serializer.data)
            print serializer.data
            
        return JSONResponse(cores_js)


class ImportaCategoria(View):
    template_name = 'categoria/importa.html'

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
                novaCategoria = Categoria(codigo=cod, descricao=desc)
                novaCategoria.save()
                i += 1
            except:
                pass

        return render(request, self.template_name, {'qtd': i, 'envio': True})
