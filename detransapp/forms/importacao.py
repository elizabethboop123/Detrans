from django import forms


class FormArquivo(forms.Form):
    arquivo = forms.FileField()
