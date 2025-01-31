from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render,get_object_or_404, redirect

from contato.models import Contato
from django import forms

class ContactForms(forms.ModelForm):
    class Meta:
        model = Contato
        fields = (
            'first_name', 'last_name','phone',
        )

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