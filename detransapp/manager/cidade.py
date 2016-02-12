from datetime import datetime

from django.db import models


class CidadeManager(models.Manager):
    def get_cidades_sicronismo(self, uf_id, data=None):
        query = self.filter()
        if data:
            data = datetime.strptime(data, '%d/%m/%Y %H:%M:%S')
            query = query.filter(data_alterado__gt=data)
            return query.all()
        return query.all()
