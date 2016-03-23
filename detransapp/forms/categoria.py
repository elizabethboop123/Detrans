from django import forms

from detransapp.models import Categoria


class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"
