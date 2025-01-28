from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Q
from contato.models import Contato
from django.core.paginator import Paginator

def create(request):
    
    context = {
       
    }
    
    return render(
        request,
        'create/index.html',
        context
    )