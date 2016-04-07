# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View

from detransapp.forms.lei import FormLei
from detransapp.models.lei import Lei


class CadastroLeisView(View):
    template = 'leis/salvar.html'

    def get(self, request, condutor_id=None):

        if condutor_id:
            leis = Lei.objects.get(pk=condutor_id)
            form = FormLei(instance=leis)
        else:
            form = FormLei()

        return render(request, self.template, {'form': form})

    def post(self, request, condutor_id=None):

        if condutor_id:
            leis = Lei.objects.get(pk=condutor_id)
            form = FormLei(instance=leis, data=request.POST)
        else:

            form = FormLei(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

        return render(request, self.template, {'form': form})


class ConsultaLeisView(View):
    template_name = 'leis/consulta.html'

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

        leis_page = Lei.objects.get_page(page, procurar)

        return render(request, self.template_name, {'leis': leis_page, 'procurar': procurar})

    def get(self, request):

        return self.__page(request)

    def post(self, request):

        return self.__page(request)
