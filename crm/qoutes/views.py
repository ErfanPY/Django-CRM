import os

import weasyprint
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import mail
from django.http import HttpResponse
from django.shortcuts import redirect, render

from qoutes.forms import QouteProductDetailForm, QoutesForm
from qoutes.models import Emails, Qoute, QouteProductDetail


def get_pdf(request, pk):
    """
        Get qoute detail based on pk and return a pdf.
    """

    qoute = Qoute.objects.get(pk=pk)

    rendred_html = render(request, 'qoutes/qoutes_info.html', {
        'qoute':qoute,
        'qouteProducts':QouteProductDetail.objects.filter(qoute=qoute)
    })

    pdf = weasyprint.HTML(string=rendred_html.content).write_pdf()
    return pdf


@login_required
def send_email_view(request, pk):
    """
        Gets a pk and make qoute pdf from that pk
        then returns a redirect to qoute list.
    """

    pdf = get_pdf(request, pk)
    reciver = os.environ.get('EMAIL_HOST_USER')
    # response = HttpResponse(pdf, content_type='application/pdf')
    email = mail.EmailMessage(
        subject='پیش فاکتور',
        from_email=os.environ.get('EMAIL_HOST_USER'),
        body="پیش فاکتور محصولات",
        to=[reciver]
    )
    
    email.attach("qoute.pdf", pdf, 'application/pdf')
    email.send()

    email_inst = Emails(reciver=reciver, status='موفقیت', sender=request.user)
    email_inst.save()

    messages.success(request, 'Successfully sent email.')
    return redirect('qoutes:list-qoutes')


@login_required
def pdf_view(request, pk):
    """
        Makes the pdf and send HttpResponse
    """

    pdf = get_pdf(request, pk)

    response = HttpResponse(pdf, content_type='application/pdf')
    return response


@login_required
def create_qoutes_view(request):
    """
        Return a html contains qoute creation form 
    """

    form_instance = QoutesForm()
    product_form = QouteProductDetailForm() 

    return render(request, 'qoutes/qoutes_form.html', {
        'form': form_instance,
        'product_form': product_form,
        'page_title': 'Create a qoute',
        'form_method': 'POST',
        'form_action': '/qoutes/api/qoute/',
        'product_form_action': '/qoutes/api/product/',
        'reset_form': True,
        'success_message': 'successfuly created qoutes.',
        'product_error_message': 'adding product failed.',
    })


@login_required
def list_qoutes_view(request):
    """
        Returns a html with a empty table to filled by ajax.
    """

    return render(request, 'qoutes/qoutes_list.html', {
        'page_title': 'qoutes list'
    })
