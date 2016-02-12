from django import forms

from detransapp.models import Especie


class FormEspecie(forms.ModelForm):
    class Meta:
        model = Especie
        fields = "__all__"
