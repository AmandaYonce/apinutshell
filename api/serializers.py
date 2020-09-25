from rest_framework import serializers
from .models import *


class ManufactureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "name", "website"]


class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ["id", "style"]


class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ["id", "color_name"]


class ShoeSizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeSize
        fields = ["id", "size"]


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandName
        fields = ["id", "brand"]


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeMaterial
        fields = ["id", "material"]
    

class FastenerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FastenType
        fields = ["id", "fastener"]
    

class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    manufacturer = ManufactureSerializer()
    brand = BrandSerializer()
    shoe_type = ShoeTypeSerializer()
    color = ShoeColorSerializer()
    size = ShoeSizeSerializer()
    material = MaterialSerializer()
    fastener = FastenerSerializer()

    class Meta:
        model = Shoe
        fields = ["id", "manufacturer", "brand", "shoe_type", "color", "size", "material", "fastener"]

# serializers.StringRelatedField()
