from django import forms

from detransapp.models import DET


class FormDet(forms.ModelForm):
    class Meta:
        model = DET
        fields = "__all__"
