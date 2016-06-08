from django.db import models
from infracao import Infracao


class Image(models.Model):

	
	infracao = models.ForeignKey(Infracao)
	photo = models.ImageField(null=True)

	class Meta:
		app_label = "detransapp"
