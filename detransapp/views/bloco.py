# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from datetime import datetime
from detransapp.forms.bloco import FormBloco
from detransapp.models import Bloco
# Daqui para baixo -> Lucas
from detransapp.serializers import BlocoSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator
from detransapp.decorators import validar_imei
from rest_framework.response import Response
# Fim do Lucas

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
    
        form = FormBloco(request.POST)
        
        if form.is_valid():
            
            post = form.save(commit=False)
            post.usuario = request.user
            
            # Controle de bloco campo 'ativo'
            bloco = Bloco.objects.filter(ativo='TRUE')
            if len(bloco) >= 2:
                post.ativo=False         
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

        blocos_page = Bloco.objects.get_page(page, procurar)

        return render(request, self.template_name, {'blocos': blocos_page, 'procurar': procurar})

    def get(self, request):

        return self.__page(request)

    def post(self, request):

        return self.__page(request)


# View que mandará as informações para o client

class GetBlocoRestView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, AllowAny)
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer


    # @method_decorator(validar_imei())
    def post(self, request):
        
        serializer = BlocoSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(usuario=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


