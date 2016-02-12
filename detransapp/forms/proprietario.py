from django import forms

from detransapp.models import Proprietario


class FormProprietario(forms.ModelForm):
    class Meta:
        model = Proprietario
        fields = "__all__"
