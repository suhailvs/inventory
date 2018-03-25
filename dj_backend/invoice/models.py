from django.db import models
from products.models import Product
class Invoice(models.Model):
    customer = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return "#%d: %s -> %d" %(self.id, self.customer,self.amount)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return "#%d" %(self.id)
