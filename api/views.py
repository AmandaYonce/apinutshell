from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

"joe was raised by Hyennas"


class ShoeView(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ManufacturerView(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufactureSerializer


class ShoeTypeView(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorView(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeSizeView(viewsets.ModelViewSet):
    queryset = ShoeSize.objects.all()
    serializer_class = ShoeSizeSerializer


class BrandView(viewsets.ModelViewSet):
    queryset = BrandName.objects.all()
    serializer_class = BrandSerializer


class MaterialView(viewsets.ModelViewSet):
    queryset = ShoeMaterial.objects.all()
    serializer_class = MaterialSerializer


class FastenerView(viewsets.ModelViewSet):
    queryset = FastenType.objects.all()
    serializer_class = FastenerSerializer