# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View

from detransapp.forms.bloco import FormBloco
from detransapp.models import Bloco


class CadastroBlocoView(View):
    template = 'bloco/salvar.html'

    def get(self, request, bloco_id=None):

        if bloco_id:
            bloco = Bloco.objects.get(pk=bloco_id)
            form = FormBloco(instance=bloco)
        else:
            form = FormBloco()

        return render(request, self.template, {'form': form})

    def post(self, request, bloco_id=None):

        if bloco_id:
            bloco = Bloco.objects.get(pk=bloco_id)
            form = FormBloco(instance=bloco, data=request.POST)
        else:

            form = FormBloco(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

        return render(request, self.template, {'form': form})


class ConsultaBlocoView(View):
    template_name = 'bloco/consulta.html'

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

        blocos_page = Bloco.objects.get_page(page, procurar)

        return render(request, self.template_name, {'blocos': blocos_page, 'procurar': procurar})

    def get(self, request):

        return self.__page(request)

    def post(self, request):

        return self.__page(request)
