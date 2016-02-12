from django import forms

from detransapp.models.lei import Lei


class FormLei(forms.ModelForm):
    class Meta:
        model = Lei
        fields = "__all__"
