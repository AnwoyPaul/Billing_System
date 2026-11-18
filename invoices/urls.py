from django.contrib import admin
from django.urls import path
from invoices import views
urlpatterns=[
  path(
    'admin/',
    admin.site.urls
  ),
  path(
    'cust/',
    views.show_invoices,
    name='Customer-name'
  )
 

]
