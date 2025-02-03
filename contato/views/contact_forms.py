from django import forms
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render,get_object_or_404, redirect

from contato.models import Contato

class ContactForms(forms.ModelForm):
    class Meta:
        model = Contato
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

def create(request):
    #print(request.method)

    if request.method == 'POST':
        context = {
                'form': ContactForms(request.POST)
            }
    
        return render(
            request,
            'contato/create.html',
            context
        )
    
    context = {
       'form': ContactForms()
    }
    
    return render(
        request,
        'contato/create.html',
        context
    )