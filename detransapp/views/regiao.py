from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from detransapp.serializers import RegiaoSerializer
from detransapp.rest import JSONResponse
from detransapp.models import Regiao


class GetRegioesRestView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request):

        if 'data' in request.POST:
            regioes = Regiao.objects.get_regioes_sicronismo(request.POST['data'])
        else:
            regioes = Regiao.objects.get_regioes_sicronismo()
        regios_js = []
        for regiao in regioes:
            serializer = RegiaoSerializer(regiao)
            regios_js.append(serializer.data)
        print('regios_js : ', regios_js)
        return JSONResponse(regios_js)
