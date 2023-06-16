from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app.models import *
from app.serializers import *
class ProductCrudActions(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    