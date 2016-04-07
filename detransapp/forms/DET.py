from django import forms

from detransapp.models.DET import Configuracao_DET


class FormDet(forms.ModelForm):
    class Meta:
        model = Configuracao_DET
        fields = "__all__"
