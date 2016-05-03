# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View

from detransapp.forms.dispositivo import FormDispositivo
from detransapp.models import Dispositivo


class CadastroDispositivoView(View):
    template = 'dispositivo/salvar.html'

    def get(self, request, dispositivo_id=None):

        if dispositivo_id:
            dispositivo = Dispositivo.objects.get(pk=dispositivo_id)
            form = FormDispositivo(instance=dispositivo)
        else:
            form = FormDispositivo()

        return render(request, self.template, {'form': form})

    def post(self, request, dispositivo_id=None):

        if dispositivo_id:
            
            dispositivo = Dispositivo.objects.get(pk=dispositivo_id)
            form = FormDispositivo(instance=dispositivo, data=request.POST)
        else:

            form = FormDispositivo(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

        return render(request, self.template, {'form': form})


class ConsultaDispositivoView(View):
    template_name = 'dispositivo/consulta.html'

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

        dispositivoes_page = Dispositivo.objects.get_page(page, procurar)

        return render(request, self.template_name, {'dispositivos': dispositivoes_page, 'procurar': procurar})

    def get(self, request):

        return self.__page(request)

    def post(self, request):

        return self.__page(request)
