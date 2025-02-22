from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Q
from contato.models import Contato
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    contacts = Contato.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj':page_obj,
        'site_title': 'Contato -'
    }
    
    return render(
        request,
        'contato/index.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contato.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains = search_value)|
            Q(last_name__icontains = search_value)|
            Q(phone__icontains = search_value)|
            Q(email__icontains = search_value)
        )\
        .order_by('-id')
    
    paginator = Paginator(contacts, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj':page_obj,
        'site_title': 'Search -',
        'search_value': search_value,
    }
    
    return render(
        request,
        'contato/index.html',
        context
    )


def contact(request, contact_id):
    #single_contact = Contato.objects.get(pk=contact_id)
    single_contact = get_object_or_404(Contato, pk=contact_id, show=True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    
    context = {
        'contact':single_contact,
        'site_title': site_title
    }
    
    return render(
        request,
        'contato/contato.html',
        context
    )