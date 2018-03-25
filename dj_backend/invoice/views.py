from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Invoice, InvoiceItem
from .serializers import InvoiceSerializer

class InvoiceDetail(APIView):
    def get_object(self, pk):
        try:
            return Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        invoice = self.get_object(pk)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

class InvoiceList(APIView):
    """
    List all Invoice, or create a new Invoice.
    """
    def get(self, request, format=None):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print (request.data)
        invoice = Invoice.objects.create(customer=request.data['customer'],amount=request.data['total'])
        for item in request.data['items']:
            InvoiceItem.objects.create(invoice=invoice,product_id=item['id'],quantity=item['qty'])
        """
        {'customer': 'sumesh', 'total': 100, 'items': [{'id': 1, 'name': 'sugar', 'price': 30, 'qty': '3', 'total': 90}, {'id': 2, 'name': 'salt', 'price': 10, 'qty': 1, 'total': 10}]}
        """
        #serializer = SnippetSerializer(data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('post')#serializer.errors, status=status.HTTP_400_BAD_REQUEST)
