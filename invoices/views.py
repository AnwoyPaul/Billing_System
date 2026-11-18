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


from django.shortcuts import render

def show_invoices(request):

    data = {
            'all_invoices': [
            {'number': 1, 'customer': 'Likhon', 'amount': 5000},
            {'number': 2, 'customer': 'APL', 'amount': 6000},
            {'number': 3, 'customer': 'Alikhon', 'amount': 7000},
        ]
    }

    return render(request, "invoices/cust.html", data)
