
from django.shortcuts import render,redirect

from contato.forms import ContactForms



def create(request):
    #print(request.method)

    if request.method == 'POST':

        form = ContactForms(request.POST)
        context = {
                'form': form
            }
        if form.is_valid():
            form.save()
            return redirect('contact:create')
    
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