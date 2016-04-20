from django import forms

from detransapp.models import TipoVeiculo


class FormTipoVeiculo(forms.ModelForm):
    class Meta:
        model = TipoVeiculo
        fields = "__all__"
