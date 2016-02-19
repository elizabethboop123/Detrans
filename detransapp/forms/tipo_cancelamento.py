from django import forms

from detransapp.models import TipoCancelamento


class FormTipoCancelamento(forms.ModelForm):
    class Meta:
        model = TipoCancelamento
        fields = "__all__"
