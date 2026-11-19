from django.contrib import admin
from .models import Invoice

class InvoiceAdmin(admin.ModelAdmin):
  list_display =[
    'invoicenum','cname','amount','date_created','paid'
  ]
  search_fields=['cname','invoicenum']
  list_filter

admin.site.register(Invoice,InvoiceAdmin)
