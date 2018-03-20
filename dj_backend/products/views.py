from django.shortcuts import render

# Create your views here.
from .serializers import ProductSerializer
from rest_framework import viewsets
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.order_by('-created_date')
	serializer_class = ProductSerializer
