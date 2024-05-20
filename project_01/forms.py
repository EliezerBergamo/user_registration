from django import forms
from project_01.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'id': 'ID',
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'cpf': 'CPF',
            'email_funcional': 'Email',
            'data_cadastro': 'Data e hora de cadastro'
        }
