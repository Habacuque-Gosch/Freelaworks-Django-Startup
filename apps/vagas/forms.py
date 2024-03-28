from django import forms
from apps.vagas.models import Vagas



class VagasForms(forms.ModelForm):
    class Meta:
        model = Vagas
        exclude = ['publicada', 'usuario','data_publicada']
        labels = {
            'descricao' : 'Descrição',
            # 'data_publicada' : 'Data de registro',
            'nome' : 'nome da vaga',
            'usuario' : ''
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'campo-user'}),
            'numero_telefone': forms.TextInput(attrs={'class': 'campo-user'}),
            'tipo_de_vaga': forms.Select(attrs={'class': ''}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'local': forms.TextInput(attrs={'class': 'campo-user'}),
            'salario': forms.TextInput(attrs={'class': 'campo-user'}),
            # 'data_publicada': forms.DateInput(
            #     format= '%d/%m/%Y',
            #     attrs={
            #         'type': 'date', 
            #         'class': 'form-control'}),

        }

class VagasFormsSave(forms.ModelForm):
    class Meta:
        model = Vagas
        exclude = ['publicada', 'data_publicada', 'usuario']
        labels = {
            'descricao' : 'Descrição',
            # 'data_publicada' : 'Data de registro',
            'nome' : 'nome da vaga',
            'usuario' : 'Usuário'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'campo-user'}),
            'numero_telefone': forms.TextInput(attrs={'class': 'campo-user'}),
            'tipo_de_vaga': forms.Select(attrs={'class': ''}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'local': forms.TextInput(attrs={'class': 'campo-user'}),
            'salario': forms.TextInput(attrs={'class': 'campo-user'}),
            # 'data_publicada': forms.DateInput(
            #     format= '%d/%m/%Y',
            #     attrs={
            #         'type': 'date', 
            #         'class': 'form-control'}),
            # 'usuario': forms.Select(attrs={'class': 'campo-user'})
        }
        