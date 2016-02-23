from django import forms
from django.contrib.auth.models import User
import datetime
from detransapp.models import Bloco


class FormBloco(forms.ModelForm):
    

    class Meta:
        model = Bloco
        fields = ('inicio_intervalo', 'fim_intervalo', 'ativo', 'contador', )
