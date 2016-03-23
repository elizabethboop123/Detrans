from django import forms

from detransapp.models import ConfigSinc


class FormConfigSinc(forms.ModelForm):
    class Meta:
        model = ConfigSinc
        fields = "__all__"
