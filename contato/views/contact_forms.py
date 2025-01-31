from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render,get_object_or_404, redirect

from contato.models import Contato

def create(request):
    
    
    context = {
       
    }
    
    return render(
        request,
        'contato/create.html',
        context
    )