from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class InvoiceList(APIView):
    """
    List all Invoice, or create a new Invoice.
    """
    def get(self, request, format=None):
        #snippets = Snippet.objects.all()
        #serializer = SnippetSerializer(snippets, many=True)
        return Response({'hai'})#serializer.data)

    def post(self, request, format=None):
        print (request.data)
        #serializer = SnippetSerializer(data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('post')#serializer.errors, status=status.HTTP_400_BAD_REQUEST)
