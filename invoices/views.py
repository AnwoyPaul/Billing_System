from django.views.generic import TemplateView,ListView,DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# Function based view
# def add_invoices(request):
#   if request.method=='POST':
#     form = InvoiceForm(request.POST)
#     if form.is_valid():






# class Homepageview(Templateview):#html page has then just pass the value
#   template_name='invoices/home.html'
# 
# def show_invoices(request):
#   data = {
#     'customer_name':"Rahul",
#     'invoice_total': 15000,
#   }
#   return render(request,"templates/invoices_list",data)

# Create New Record
from django.shortcuts import render
from .models import Invoice
def create_invoice(request):
    Invoice.objects.create (
        cname='Likhon',
        invoicenum='AP=001',
        amount=15000,
        paid=False
    
        )
    return render(request,'invoices/invoice_list.html',{})
# Ferch
def show_one_invoice(request):
    invoice=Invoice.objects.get(invoicenum='AP=001')
    return render(request,'invoices/invoice_details.html',{})

# Filter Method
def show_unpaid_invoices(request):
    unpaid_invoices=Invoice.objects.filter(paid=False)
    data= {
        'unpaid_invoices':unpaid_invoices
    }
    return render(request,'invoices/invoice_list.html',data)
# Update
def mark_as_paid(request):
    Invoice.objects.filter(invoicenum='AP=001').update(paid=True)

    allin= Invoice.objects.filter(paid=False)
    data={
        'allin':allin
    }
    return render(request,'invoices/invoice_list.html',{data})


def show_invoices(request):

    data = {
            'all_invoices': [
            {'number': 1, 'customer': 'Likhon', 'amount': 5000},
            {'number': 2, 'customer': 'APL', 'amount': 6000},
            {'number': 3, 'customer': 'Alikhon', 'amount': 7000},
        ]
    }

    return render(request, "invoices/cust.html", data)
