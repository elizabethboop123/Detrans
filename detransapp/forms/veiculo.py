from django import forms

from detransapp.models import Veiculo, UF, Cidade


class FormVeiculo(forms.ModelForm):
    uf = forms.ModelChoiceField(queryset=UF.objects.all())

    def __init__(self, uf_id, *args, **kwargs):
        super(FormVeiculo, self).__init__(*args, **kwargs)
        self.fields['cidade'] = forms.ModelChoiceField(queryset=Cidade.objects.filter(uf_id=uf_id))

    class Meta:
        model = Veiculo
        fields = "__all__"
