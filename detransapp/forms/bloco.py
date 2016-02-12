from django import forms
from django.contrib.auth.models import User

from detransapp.models import Bloco


class FormBloco(forms.ModelForm):
    def save(self, request, commit=True):
        bloco = super(FormBloco, self).save(commit=False)
        user = User.objects.filter(id=request.user.id)
        bloco.author = user[0]
        if commit:
            bloco.save()
        return bloco

    class Meta:
        model = Bloco
        exclude = ('author',)
