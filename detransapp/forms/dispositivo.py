from django import forms

from detransapp.models import Dispositivo


class FormDispositivo(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = "__all__"
