from django import forms
from django.contrib.auth.models import User
<<<<<<< HEAD

=======
import datetime
>>>>>>> 42530833b14b0f1113b8362e49e66e19662d0de8
from detransapp.models import Bloco


class FormBloco(forms.ModelForm):
<<<<<<< HEAD
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
=======
    

    class Meta:
        model = Bloco
        fields = ('inicio_intervalo', 'fim_intervalo', 'ativo', )
>>>>>>> 42530833b14b0f1113b8362e49e66e19662d0de8
