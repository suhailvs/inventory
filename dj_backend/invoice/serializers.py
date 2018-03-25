from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Invoice, InvoiceItem
from django.http import JsonResponse,HttpResponse
import json
class InvoiceSerializer(ModelSerializer):
    invoiceitems = SerializerMethodField()
    class Meta:
        model = Invoice
        fields = '__all__'#('id','customer','date','amount')
    def get_invoiceitems(self, obj):
        data =[]
        #invoiceitems=[{'invoice':1,'product':{'name':'sugar','price':10},'quantity':10}]
        items = InvoiceItem.objects.filter(invoice=obj.id)
        for item in items:
            data.append({
             'invoice':item.invoice.id,
             'product':{'name':item.product.name,'price':item.product.price},
             'quantity':item.quantity
        })
        #print (data)
        return data 
