from rest_framework import serializers
from .models import *


class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "name", "website"]


class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeType
        fields = ["id", "style"]


class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ["id", "color_name"]