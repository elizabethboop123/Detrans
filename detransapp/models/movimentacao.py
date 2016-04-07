from django.db import models


class Movimentacao(models.Model):
    tempo = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()


    class Meta:
        app_label = "detransapp"
