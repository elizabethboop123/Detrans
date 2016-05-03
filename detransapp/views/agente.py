# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator

from detransapp.models import Agente_login
from detransapp.forms.agente import FormAgente
from detransapp.models.dispositivo import Dispositivo
from detransapp.models.agente import Agente
from detransapp.models.agente_login import Agente_login
from detransapp.serializers import AgenteSerializer
from detransapp.rest import JSONResponse
from detransapp.decorators import validar_imei


class CadastroAgenteView(View):
    template = 'agente/salvar.html'

    def get(self, request, agente_id=None):
        if agente_id:
            agente = Agente.objects.get(pk=agente_id)
            form = FormAgente(instance=agente)
        else:
            form = FormAgente()

        return render(request, self.template, {'form': form})

    def post(self, request, agente_id=None):

        if agente_id:
            agente = Agente.objects.get(pk=agente_id)
            form = FormAgente(request.POST, instance=agente)
        else:
            form = FormAgente(request.POST)


        if form.is_valid():
            form.is_active = True
            form.save()

            return redirect('/')

        else:
            print "agente não válido"

        
        return render(request, self.template, {'form': form})


class ConsultaAgenteView(View):
    template_name = 'agente/consulta.html'

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

        agentes_page = Agente.objects.get_page(page, procurar)

        return render(request, self.template_name, {'agentes': agentes_page, 'procurar': procurar})

    def get(self, request):

        return self.__page(request)

    def post(self, request):

        return self.__page(request)


class GetAgentesRestView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    @method_decorator(validar_imei())
    def post(self, request):
        if 'data' in request.POST:
            agentes = Agente.objects.get_agentes_sicronismo(request.POST['data'])
        else:
            agentes = Agente.objects.get_agentes_sicronismo()
        agentes_js = []
        for agente in agentes:
            serializer = AgenteSerializer(agente)
            agentes_js.append(serializer.data)
        return JSONResponse(agentes_js)


class GetControlLoginRestView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    @method_decorator(validar_imei())
    def post(self, request):
        controle = loads(request.POST['controle_login'])

        status = True

        if controle['status'] == 0:
            status = False

        # Logar
        if status == True:
            agente_login = Agente_login.objects.filter(device=controle['device'], agente=int(controle['agente']), status=True)
            if agente_login:
                return False
            else:
                agente_login = Agente_login()

                agente_login.agente = int(controle['agente'])

                dispositivo = Dispositivo.objects.get(imei=controle['device'])
                agente_login.device = dispositivo.id 

                agente_login.save()
                return True
        # Deslogar
        else:

            # Talvez utilizar o filter
            agente_login = Agente_login.objects.get(device=controle['device'], agente=int(controle['agente']), status=True)

            if agente_login:

                agente_login.status = False
                agente_login.save()
                return True

            else:
                return False
