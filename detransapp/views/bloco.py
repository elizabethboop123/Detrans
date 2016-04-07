# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View

from detransapp.forms.bloco import FormBloco
<<<<<<< HEAD
from detransapp.models import Bloco, BlocoPadrao
# Daqui para baixo -> Lucas
from django.utils import timezone
from django.contrib.auth.models import User
from detransapp.rest import JSONResponse
from detransapp.models.bloco_padrao import BlocoPadrao
from detransapp.models.infracao import Infracao 
from detransapp.serializers import BlocoSerializer
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator
from detransapp.decorators import validar_imei
from rest_framework.response import Response
from rest_framework import permissions
from detransapp.permissions import IsOwnerOrReadOnly
# Fim do Lucas
=======
from detransapp.models import Bloco

>>>>>>> 1a7e28163ca8c15961f8c29385178cfd18e9c58f

class CadastroBlocoView(View):
    template = 'bloco/salvar.html'

    def get(self, request, bloco_id=None):

        if bloco_id:
<<<<<<< HEAD
            
            bloco = BlocoPadrao.objects.get(pk=bloco_id)
=======
            bloco = Bloco.objects.get(pk=bloco_id)
>>>>>>> 1a7e28163ca8c15961f8c29385178cfd18e9c58f
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
<<<<<<< HEAD
            
            post = form.save(commit=False)
            
            # Controle de bloco campo 'ativo'
            bloco = BlocoPadrao.objects.filter(ativo='TRUE')
            if len(bloco) >= 1:
                post.ativo=False         
                form.save()
            else:
                form.save()
=======
            form.save()
>>>>>>> 1a7e28163ca8c15961f8c29385178cfd18e9c58f

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
<<<<<<< HEAD


# View que mandará as informações para o client

class GetBlocoRestView(APIView):

    permission_classes = (AllowAny, AllowAny)


    @method_decorator(validar_imei())
    def post(self, request):
        
        # Se não tiver registros de bloco desse usuário
        # (primeiro acesso) mande um bloco para ele!
        if not Bloco.objects.filter(usuario=request.user):
            
            print "caiu no primeiro if"
            bloco = AddBloco(request)
            # bloco.agente_campo = request.user
            bloco.save()

            bp = BlocoPadrao.objects.get(ativo=True)
            bp.contador += bp.numero_paginas

            bp.save()    

            serializer = BlocoSerializer(bloco)
            print serializer.data

            js_core = []
            js_core.append(serializer.data)



            return JSONResponse(js_core)

        # Se houver registros do usuário na tabela bloco:
        else:
            """ 
            if requisita um bloco || 1 - Verificar se o último IF bloco desse usuário está acabando 
                e então mandar um novo para ele e setar o anterior "Ativo=False".

            if usuario logou no sistema || 2 - Se o bloco dele não estiver acabando, verificar se ele
                cabou de se logar e então mandar para ele seu último bloco cadastrado 
                com o valor de "inicio_intervalo" latualizado.

                obs: Ordenação por data em ordem Decrescente:
                  >>> Bloco.objects.filter(usuario=request.user).order_by('-data')
            """
            
            bloco = Bloco.objects.filter(usuario=request.user).order_by('-data')[0]
            inf = Infracao.objects.filter(id__range=[bloco.inicio_intervalo, bloco.fim_intervalo])
            
            usr = User.objects.get(id=request.user.id)
            

            # user.last_login
            # número mínimo de páginas
            bloco_valor_max = 50
            

            ''' Se o bloco excedeu de fato seu limite, mande outro '''
            if (bloco.fim_intervalo - len(inf)) <= bloco_valor_max:
                bloco = Bloco.objects.filter(usuario=request.user).order_by('-data_alterado')[0]
                # bloco.agente_campo = request.user
                bloco.ativo = False
                bloco.save()

                bloco = AddBloco(request)
                # bloco.agente_campo = request.user
                bloco.save()

                bp = BlocoPadrao.objects.get(ativo=True)
                bp.contador += bp.numero_paginas
                bp.save()

                serializer = BlocoSerializer(bloco)
                core_js = []
                core_js.append(serializer.data)

                print "caiu na condição de falta de numero_paginas"

                return JSONResponse(core_js)

            """ Se não excedeu e mesmo assim houve a requisição, verificar se ele logou a poucos
                minutos
            """

            

            """ Se o usuário acabou de se logar então mande seu bloco"""
            
            if (timezone.now() - usr.last_login).total_seconds()/60 < 20:
                bloco = Bloco.objects.filter(usuario=request.user).order_by('-data_alterado')[0]
                # mudar a data modificado pra de agora
                bloco.data_alterado = timezone.now()
                bloco.inicio_intervalo += len(inf) 
                bloco.save()
                serializer = BlocoSerializer(bloco)
                print "caiu na condição de login"
                return JSONResponse(serializer.data)

            """ Condição para testes """
            
            
def AddBloco(request):
    bp = BlocoPadrao.objects.get(ativo=True)
    bloco = Bloco()
    bloco.inicio_intervalo = bp.contador
    bloco.fim_intervalo = bp.contador + bp.numero_paginas
    bloco.usuario = request.user 
    bloco.ativo = True
    bloco.minimo_pag_restantes = bp.minimo_pag_restantes

    return bloco

=======
>>>>>>> 1a7e28163ca8c15961f8c29385178cfd18e9c58f
