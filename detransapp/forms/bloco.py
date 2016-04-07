from django import forms
from django.contrib.auth.models import User
import datetime
from detransapp.models import BlocoPadrao


class FormBloco(forms.ModelForm):
    

    class Meta:
        model = BlocoPadrao
        fields = ('inicio_intervalo', 'fim_intervalo', 'ativo', 'numero_paginas', 'minimo_pag_restantes',)
