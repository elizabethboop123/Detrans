from django.db import models


class Sistema(models.Model):
    sigla = models.CharField(max_length=150)
    nome_completo = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='images/')
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "detransapp"
        # verbose_name= self.sigla
