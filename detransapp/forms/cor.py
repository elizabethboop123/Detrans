from django import forms

from detransapp.models import Cor


class FormCor(forms.ModelForm):
    class Meta:
        model = Cor
        fields = "__all__"
