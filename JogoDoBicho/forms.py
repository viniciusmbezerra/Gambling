from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from JogoDoBicho.models import Bicho, Cliente, Administrador, Categoria, LanceJB,  ApostaJB

class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name', 'email')

class AdministradorForm(forms.ModelForm):
    data_nasc = forms.DateField(widget=DateInput(), label='Data de Nascimento')

    class Meta:
        model = Administrador
        fields = ('cpf', 'data_nasc', 'foto')
        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXX.XXX.XXX-XX'}),
            'data_nasc': forms.DateInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'})
        }


class ClienteForm(forms.ModelForm):
    data_nasc = forms.DateField(widget=DateInput(), label='Data de Nascimento')
    
    class Meta:
        model = Cliente
        fields = ('cpf', 'data_nasc', 'foto')
        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXX.XXX.XXX-XX', 'label':'CPF'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'})
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('descricao', 'valor')


class BichoForm(forms.ModelForm):
    class Meta:
        model = Bicho
        fields = ('nome', 'grupo', 'icone', 'dezenhas')

class LanceJBForm(forms.ModelForm):
    fim = forms.DateTimeField(widget=DateTimeInput(), label='Termina em:')
    class Meta:
        model = LanceJB
        fields = ('banner', 'categoria', 'fim')
        widgets = {
            'banner': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ApostaJBForm(forms.ModelForm):
    class Meta:
        model = ApostaJB
        fields = ('escolhas',)
        exclude = ('cliente',)
        widgets = {
            'escolhas': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }