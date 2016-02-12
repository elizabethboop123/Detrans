from datetime import datetime

from django.db import models
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings


class EspecieManager(models.Manager):
    def get_page(self, page, procurar):

        if procurar is not None and procurar != '':
            especies = self.filter(Q(descricao__icontains=procurar))
        else:
            especies = self.filter()

        especies = especies.order_by('especie')

        paginator = Paginator(especies, settings.NR_REGISTROS_PAGINA)
        try:
            especies_page = paginator.page(page)
        except:
            especies_page = paginator.page(paginator.num_pages)
        print especies_page
        return especies_page

    def get_especies_sicronismo(self, data=None):
        if data:
            data = datetime.strptime(data, '%d/%m/%Y %H:%M:%S')
            query = self.filter(data_alterado__gt=data)
            return query.all()
        return self.all()
