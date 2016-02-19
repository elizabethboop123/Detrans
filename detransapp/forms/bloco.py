from django import forms
from django.contrib.auth.models import User
import datetime
from detransapp.models import Bloco


class FormBloco(forms.ModelForm):
    # def save(self, request, commit=True):
    #     bloco = super(FormBloco, self).save(commit=False)
    #     user = User.objects.filter(id=request.user.id)
    #     bloco.author = user[0]
    #     if commit:
    #         bloco.save()
    #     return bloco

    # class Meta:
    #     model = Bloco
    #     exclude = ('author',)
    # inicio_intervalo = forms.IntegerField(help_text='Inicio Intervalo')
    # fim_intervalo = forms.IntegerField(help_text='Fim Intervalo')
    # ativo = forms.BooleanField(help_text='Status')
    # class Meta:
    #     model = Bloco
    #     fields = ('inicio_intervalo','fim_intervalo','ativo',)
    # inicio_intervalo = forms.IntegerField(help_text='Inicio Intervalo')
    # fim_intervalo = forms.IntegerField(help_text='Fim Intervalo')
    # ativo = forms.BooleanField(help_text='Status')
    # contador = forms.IntegerField(help_text='Inicio Contador')

    class Meta:
        model = Bloco
        fields = ('inicio_intervalo', 'fim_intervalo', 'ativo', 'contador', )
