from django import forms

from detransapp.models import TipoInfracao


class FormTipoInfracao(forms.ModelForm):
    class Meta:
        model = TipoInfracao
        fields = "__all__"
