
from django.shortcuts import render

from contato.forms import ContactForms



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