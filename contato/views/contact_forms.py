
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse

from contato.forms import ContactForms
from contato.models import Contato



def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':

        form = ContactForms(request.POST)
        context = {
                'form': form,
                'form_action': form_action,
            }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id = contact.pk)
    
        return render(
            request,
            'contato/create.html',
            context
        )
    
    context = {
       'form': ContactForms(),
        'form_action': form_action,
    }
    
    return render(
        request,
        'contato/create.html',
        context
    )

def update(request,contact_id):
    contact = get_object_or_404(Contato, pk=contact_id, show=True)

    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':

        form = ContactForms(request.POST, instance=contact)
        context = {
                'form': form,
                'form_action': form_action,
            }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id = contact.pk)
    
        return render(
            request,
            'contato/create.html',
            context
        )
    
    context = {
       'form': ContactForms(instance=contact),
        'form_action': form_action,
    }
    
    return render(
        request,
        'contato/create.html',
        context
    )