# coding: utf-8
import datetime

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator

from detransapp.rest import JSONResponse
from detransapp.decorators import validar_imei


class SincronismoRestView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    @method_decorator(validar_imei())
    def post(self, request):
        return JSONResponse({'data': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
