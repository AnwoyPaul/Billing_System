from django.contrib import admin
from django.urls import path
from invoices import views
urlpatterns=[
    path("cust/", views.show_invoices, name="Customer-name"),
    path("list/", views.show_invoice_list, {"unpaid_only": True}, name="invoice_list"),
    path("invoices/", views.show_invoice_list, name="all_invoices"),
    path("details/<int:pk>/", views.show_one_invoice, name="invoice_detail"),
    path("details", RedirectView.as_view(pattern_name="all_invoices"), name="Details"),

]
