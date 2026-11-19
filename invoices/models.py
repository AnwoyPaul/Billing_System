from django.db import models


class Invoice(models.Model):
    cname = models.CharField(max_length=200)
    invoicenum = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    companyn = models.CharField(max_length=50)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.invoicenum