from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

"joe was raised by Hyennas"


class ManufacturerView(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufactureSerializer


class ShoeTypeView(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorView(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer