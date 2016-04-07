from django import forms
from django.contrib.auth.models import User
<<<<<<< HEAD
import datetime
from detransapp.models import BlocoPadrao
=======

from detransapp.models import Bloco
>>>>>>> 1a7e28163ca8c15961f8c29385178cfd18e9c58f


class FormBloco(forms.ModelForm):
    def save(self, request, commit=True):
        bloco = super(FormBloco, self).save(commit=False)
        user = User.objects.filter(id=request.user.id)
        bloco.author = user[0]
        if commit:
            bloco.save()
        return bloco

    class Meta:
<<<<<<< HEAD
        model = BlocoPadrao
        fields = ('inicio_intervalo', 'fim_intervalo', 'ativo', 'numero_paginas', 'minimo_pag_restantes',)
=======
        model = Bloco
        exclude = ('author',)
>>>>>>> 1a7e28163ca8c15961f8c29385178cfd18e9c58f
