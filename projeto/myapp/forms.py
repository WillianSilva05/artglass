from django import forms
from .models import Usuario, Vendas


class LoginForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['usuario', 'senha', ]


class addVendaForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['id_usuario', 'valor', ]


class editMetaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['meta', ]
