from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import forms
from organizations.models import Organization

def home(request):
    return render(request, 'web/home.html', {
        'page_title': 'Home'
    })


@login_required
def create_organizations_view(request):

    form_instance = forms.OrganizationsForm()

    return render(request, 'web/organizations_form.html', {
        'form': form_instance,
        'page_title': 'Create a organizations',
        'form_method': 'POST',
        'form_action': '/organizations/api/',
        'reset_form': True,
        'success_message': 'successfuly created organizations.',
    })


@login_required
def list_organizations_view(request):

    return render(request, 'web/organizations_list.html', {
        'page_title': 'Organizations list'
    })


@login_required
def retrieve_organizations_view(request, pk):

    return render(request, 'web/organizations_info.html', {
        'page_title': 'Organizations info'
    })


@login_required
def edit_organizations_view(request, pk):
    organizations = Organization.objects.get(pk=pk)
    
    form_instance = forms.OrganizationsForm(initial={
        'name':organizations.name,
        'province':organizations.province,
        'phone_number':organizations.phone_number,
        'workers_count':organizations.workers_count,
        'contact_fullname':organizations.contact_fullname,
        'contact_phone_number':organizations.contact_phone_number,
        'email':organizations.email,
        'products':[product.id for product in organizations.products.all()]
    })

    return render(request, 'web/organizations_form.html', {
        'form': form_instance,
        'page_title': 'Edit organizations',
        'form_method': 'PATCH',
        'form_action': '/organizations/api/{}/'.format(str(pk)),
        'success_message': 'successfuly edited organizations.',
    })
