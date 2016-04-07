from django.db import models
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings


class TipoCancelamentoManager(models.Manager):
    def get_page(self, page, procurar):

        if procurar is not None and procurar != '':
            cancelamentos = self.filter(Q(descricao__icontains=procurar))
        else:
            cancelamentos = self.filter()

        cancelamentos = cancelamentos.order_by('codigo')

        paginator = Paginator(cancelamentos, settings.NR_REGISTROS_PAGINA)
        try:
            tipos_page = paginator.page(page)
        except:
            tipos_page = paginator.page(paginator.num_pages)

        return tipos_page
