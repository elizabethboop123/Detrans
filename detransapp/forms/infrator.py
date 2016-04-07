from django import forms

from detransapp.models import Infrator


class FormInfrator(forms.ModelForm):
    class Meta:
        model = Infrator
        fields = "__all__"
