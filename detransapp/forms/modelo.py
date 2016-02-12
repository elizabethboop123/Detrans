from django import forms

from detransapp.models import Modelo


class FormModelo(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = "__all__"
