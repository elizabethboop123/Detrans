# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from datetime import datetime
from detransapp.forms.bloco import FormBloco
from detransapp.models import Bloco, BlocoPadrao, Agente_login
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

class CadastroBlocoView(View):
    template = 'bloco/salvar.html'

    def get(self, request, bloco_id=None):

        if bloco_id:
            
            bloco = BlocoPadrao.objects.get(pk=bloco_id)
            form = FormBloco(instance=bloco)
        else:

            form = FormBloco()

        return render(request, self.template, {'form': form})

    def post(self, request, bloco_id=None):
        
        bloco_id = bloco_id

        form = FormBloco(request.POST)

        is_input = True

        if bloco_id:
            bloco_padrao = BlocoPadrao.objects.get(pk=bloco_id)
            form = FormBloco(instance=bloco_padrao, data=request.POST)
            is_input = False

        else:

            form = FormBloco(request.POST)

        if form.is_valid():
            
            if is_input == True:
                post = form.save(commit=False)

                # Controle de bloco campo 'ativo'

                bloco = BlocoPadrao.objects.filter(ativo='TRUE')
                if len(bloco) >= 1:
                    post.ativo=False         
                    form.save()
                else:
                    form.save()

            else:
                
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

        blocos_page = BlocoPadrao.objects.get_page(page, procurar)

        return render(request, self.template_name, {'blocos': blocos_page, 'procurar': procurar})

    def get(self, request):

        return self.__page(request)

    def post(self, request):

        return self.__page(request)


# View que mandará as informações para o client

class GetBlocoRestView(APIView):

    
    permission_classes = (IsAuthenticated, AllowAny)


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
                        
            bloco = Bloco.objects.filter(usuario=request.user).order_by('-data')[0]
            inf = Infracao.objects.filter(id__range=[bloco.inicio_intervalo, bloco.fim_intervalo])
            
            # Datetime Login User
            usr = Agente_login.objects.get(agente_id=request.user.id, status=True)
                        

            
            
            if (timezone.now() - usr.data_login).total_seconds()/60 < 7:

                print "caiu no envia-bloco-login"
                
                bloco = Bloco.objects.filter(usuario=request.user).order_by('-data_alterado')
                core_js = []

                if len(bloco) > 1:
                    inf1 = Infracao.objects.filter(id__range=[bloco[1].inicio_intervalo, bloco[1].fim_intervalo])
                    if (bloco[1].fim_intervalo - len(inf1)) <= bloco[1].minimo_pag_restantes:
                        bloco = Bloco.objects.get(id=bloco[1].id)
                        bloco.inicio_intervalo += len(inf1)
                        bloco.data_alterado = timezone.now() 
                        bloco.save()
                        serializer = BlocoSerializer(bloco)
                        core_js.append(serializer.data)

                              
                bloco = Bloco.objects.get(id=bloco[0].id)
                bloco.data_alterado = timezone.now()
                bloco.inicio_intervalo += len(inf) 
                bloco.save()
                serializer = BlocoSerializer(bloco)
                
                core_js.append(serializer.data)
                return JSONResponse(core_js)


            else:

                if (bloco.fim_intervalo - len(inf)) <= bloco.minimo_pag_restantes:
                    
                    bloco = Bloco.objects.filter(usuario=request.user).order_by('-data_alterado')[0]
                    
                    bloco.ativo = False
                    bloco.save()

                    bloco = AddBloco(request)
                    
                    bloco.save()

                    bp = BlocoPadrao.objects.get(ativo=True)
                    bp.contador += bp.numero_paginas
                    bp.save()

                    serializer = BlocoSerializer(bloco)
                    core_js = []
                    core_js.append(serializer.data)

                    print "caiu na condição de falta de numero_paginas"

                    return JSONResponse(core_js)

               
                
            
def AddBloco(request):
    bp = BlocoPadrao.objects.get(ativo=True)
    bloco = Bloco()
    bloco.inicio_intervalo = bp.contador
    bloco.fim_intervalo = bp.contador + bp.numero_paginas
    bloco.usuario = request.user
    bloco.ativo = True
    bloco.minimo_pag_restantes = bp.minimo_pag_restantes

    return bloco

