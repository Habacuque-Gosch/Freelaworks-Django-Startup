from django import forms
from apps.usuarios.models import Resumo



class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Ex: Habacuque Gosch"
            }
        )
    )
    senha_login = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Ex: Habacuque Gosch"
            }
        )
    )
    
    email = forms.CharField(
        label="Seu de número telefone",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Ex: 48000000000"
            }
        )
    )

    senha_cadastro = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Digite sua senha"
            }
        )
    )

    senha_confirma = forms.CharField(
        label="Confirme sua Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome

class ResumoForms(forms.ModelForm):
    class Meta:
        model = Resumo
        exclude = ['']
        labels = {
            'nome_completo' : 'Nome completo',
            'telefone' : 'Telefone',
            'titulo_profissional' : 'Título profissional',
            'descricao_pessoal' : 'Conte-nos sobre você',
            'resumo_experiencia_profissional' : 'Resuma a sua experiência profissional'
        }

        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'campo-user'}),
            'telefone': forms.TextInput(attrs={'class': 'campo-user'}),
            'titulo_profissional': forms.TextInput(attrs={'class': 'campo-user'}),
            'descricao_pessoal': forms.Textarea(attrs={'class': 'form-control'}),
            'resumo_experiencia_profissional': forms.Textarea(attrs={'class': 'form-control'}),
            # 'pago': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class ResumoFormsSave(forms.ModelForm):
    class Meta:
        model = Resumo
        exclude = ['usuario_edit']
        labels = {
            'nome_completo' : 'Nome completo',
            'telefone' : 'Telefone',
            'titulo_profissional' : 'Título profissional',
            'descricao_pessoal' : 'Conte-nos sobre você',
            'resumo_experiencia_profissional' : 'Resuma a sua experiência profissional'
        }

        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'campo-user'}),
            'telefone': forms.TextInput(attrs={'class': 'campo-user'}),
            'titulo_profissional': forms.TextInput(attrs={'class': 'campo-user'}),
            'descricao_pessoal': forms.Textarea(attrs={'class': 'descricao-pessoal'}),
            'resumo_experiencia_profissional': forms.Textarea(attrs={'class': 'resumo-experiencia'}),
            # 'pago': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
# class CurriculoForms(forms.ModelForm):
    # class Meta:
        # model = Curriculo
        # exclude = ['']
        # labels = {
        #     'curriculo' : '',
        # }

        # widgets = {
        #     'curriculo': forms.FileInput(attrs={'class': 'form-control'})
        # }             


        