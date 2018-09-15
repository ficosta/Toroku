from django import forms

from .models import Visitante

class DateInput(forms.DateInput):
    input_type = 'date'


class VisitanteForm(forms.ModelForm):

    class Meta:
        model = Visitante
        fields = ('nome', 'email','telefone','documento','aniversario','sexo','tipo','CodigoBarra')
        widgets = {
            'aniversario': DateInput()
        }
