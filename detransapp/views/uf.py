from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator

from detransapp.models import UF
from detransapp.serializers import UFSerializer
from detransapp.rest import JSONResponse
from detransapp.decorators import validar_imei


class GetUFsRestView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    @method_decorator(validar_imei())
    def post(self, request):
        if 'data' in request.POST:
            ufs = UF.objects.get_ufs_sicronismo(request.POST['data'])
        else:
            ufs = UF.objects.get_ufs_sicronismo()

        json_ufs = []
        for uf in ufs:
            serializer = UFSerializer(uf)
            json_ufs.append(serializer.data)
        return JSONResponse(json_ufs)
