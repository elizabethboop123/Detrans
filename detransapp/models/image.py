from django.db import models
from infracao import Infracao


class Image(models.Model):
    id_image = models.IntegerField(primary_key=True)
    infracao = models.ForeignKey(Infracao)
    photo = models.ImageField(null=True)
    

    # objects = CidadeManager()

    def __unicode__(self):
        return self.nome

    class Meta:
        app_label = "detransapp"
