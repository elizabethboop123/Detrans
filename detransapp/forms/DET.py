from django import forms

<<<<<<< HEAD
from detransapp.models import DET
=======
from detransapp.models.DET import Configuracao_DET
>>>>>>> 42530833b14b0f1113b8362e49e66e19662d0de8


class FormDet(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model = DET
=======
        model = Configuracao_DET
>>>>>>> 42530833b14b0f1113b8362e49e66e19662d0de8
        fields = "__all__"
