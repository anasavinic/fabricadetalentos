from django.forms import forms
from cadastros.models import Aluno


class AlunoForm(forms.Form):

    class Meta:
        model = Aluno
        fields = '__all__'

