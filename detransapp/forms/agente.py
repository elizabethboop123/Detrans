from django import forms
from detransapp.models import Agente


class FormAgente(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput)

	def save(self, commit=True):
		agente = super(FormAgente, self).save(commit=False)
		agente.set_password(self.cleaned_data['password'])
		if commit:
			agente.save()
		return agente

	class Meta:
		model = Agente
		exclude = ('movimentos','regioes','email','date_joined','is_staff','user_permissions','groups','last_login',)

