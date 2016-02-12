# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View

from detransapp.forms.DET import FormDET
from detransapp.models import Configuracao_DET


class CadastroDETView(View):
    template = 'det/salvar.html'

    def get(self, request, det_id=None):

        if det_id:
            det = Configuracao_DET.objects.get(pk=det_id)
            form = FormDET(instance=det)
        else:
            form = FormDET()

        return render(request, self.template, {'form': form})

    def post(self, request, det_id=None):

        if det_id:
            cor = Configuracao_DET.objects.get(pk=det_id)
            form = FormDET(instance=cor, data=request.POST)
        else:

            form = FormDET(request.POST)

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

        cores_page = Configuracao_DET.objects.get_page(page, procurar)

        return render(request, self.template_name, {'cores': cores_page, 'procurar': procurar})

    def get(self, request):
        return self.__page(request)

    def post(self, request):
        return self.__page(request)
