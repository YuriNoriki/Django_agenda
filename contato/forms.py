from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForms(forms.ModelForm):

    first_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': 'classe-a classe-b',
                    'placeholder': 'Aqui veio do init',
                }
            ),
            label='Primeiro Nome',
            help_text='Texto de ajuda para seu usuário',
        )
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Contato
        fields = (
            'first_name', 'last_name','phone',
        )

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            None,
            ValidationError(
                "mensagem de error",
                code = 'invalid'
            )
        )

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )

        return super().clean()