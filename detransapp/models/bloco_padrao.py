from django.db import models
from django.contrib.auth.models import User
from detransapp.manager import BlocoManager

class BlocoPadrao(models.Model):
	
	# usuario = models.ForeignKey(User)
	inicio_intervalo = models.IntegerField()
	fim_intervalo = models.IntegerField()
	data = models.DateTimeField(auto_now_add=True)
	contador = models.IntegerField(default=0)
	ativo = models.BooleanField(default=True)
	numero_paginas = models.IntegerField(default=1000)
	minimo_pag_restantes = models.IntegerField(null=True)

	objects = BlocoManager()