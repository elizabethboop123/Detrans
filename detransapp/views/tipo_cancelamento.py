# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View

from detransapp.forms.tipo_cancelamento import FormTipoCancelamento
from detransapp.models import TipoCancelamento


class CadastroCancelamentoView(View):
    template = 'tipo_cancelamento/salvar.html'

    def get(self, request, cancelamento_id=None):

        if cancelamento_id:
            cancelamento = TipoCancelamento.objects.get(pk=cancelamento_id)
            form = FormTipoCancelamento(instance=cancelamento)
        else:
            form = FormTipoCancelamento()

        return render(request, self.template, {'form': form})

    def post(self, request, cancelamento_id=None):

        if cancelamento_id:
            cancelamento = TipoCancelamento.objects.get(pk=cancelamento_id)
            form = FormTipoCancelamento(instance=cancelamento, data=request.POST)
        else:

            form = FormTipoCancelamento(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

        return render(request, self.template, {'form': form})


class ConsultaCancelamentoView(View):
    template_name = 'tipo_cancelamento/consulta.html'

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

        cancelamentos_page = TipoCancelamento.objects.get_page(page, procurar)

        return render(request, self.template_name, {'cancelamentos': cancelamentos_page, 'procurar': procurar})

    def get(self, request):

        return self.__page(request)

    def post(self, request):

        return self.__page(request)
