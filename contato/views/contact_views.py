from django.shortcuts import render
from contato.models import Contato

# Create your views here.

def index(request):
    contacts = Contato.objects.all()
    
    context = {
        'contacts':contacts
    }
    
    return render(
        request,
        'contato/index.html',
        context
    )