from django import forms

from detransapp.models import DET


class FormDET(forms.ModelForm):
    class Meta:
        model = DET
        fields = "__all__"
