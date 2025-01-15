from django.shortcuts import render,get_object_or_404
from contato.models import Contato

# Create your views here.

def index(request):
    contacts = Contato.objects.filter(show=True).order_by('-id')[:20]
    
    context = {
        'contacts':contacts
    }
    
    return render(
        request,
        'contato/index.html',
        context
    )

def contact(request, contact_id):
    #single_contact = Contato.objects.get(pk=contact_id)
    single_contact = get_object_or_404(Contato, pk=contact_id, show=True)
    
    context = {
        'contact':single_contact,
    }
    
    return render(
        request,
        'contato/contato.html',
        context
    )