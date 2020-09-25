from django.core.management.base import BaseCommand
from api.models import Manufacturer, ShoeType, ShoeColor, ShoeSize, BrandName, ShoeMaterial, FastenType, Shoe


class Command(BaseCommand):
    help = 'some help string'
        
    def handle(self, *args, **options):

        ShoeType.objects.bulk_create([
            ShoeType(style='sneaker'),
            ShoeType(style='dress'),
            ShoeType(style='sandal'),
            ShoeType(style='boot'),
            ShoeType(style='other')
        ])

        ShoeColor.objects.bulk_create([
            ShoeColor(color_name='white'),
            ShoeColor(color_name='black'),
            ShoeColor(color_name='red'),
            ShoeColor(color_name='orange'),
            ShoeColor(color_name='yellow'),
            ShoeColor(color_name='green'),
            ShoeColor(color_name='blue'),
            ShoeColor(color_name='indigo'),
            ShoeColor(color_name='violet')
        ])

        ShoeSize.objects.bulk_create([
            ShoeSize(size='5'),
            ShoeSize(size='6'),
            ShoeSize(size='7'),
            ShoeSize(size='8'),
            ShoeSize(size='9'),
        ])

        BrandName.objects.bulk_create([
            BrandName(brand='nike'),
            BrandName(brand='addidas'),
            BrandName(brand='rainbow'),
            BrandName(brand='vans'),
            BrandName(brand='other'),
        ])

        ShoeMaterial.objects.bulk_create([
            ShoeMaterial(material='leather'),
            ShoeMaterial(material='canvas'),
            ShoeMaterial(material='other'),        
        ])

        FastenType.objects.bulk_create([
            FastenType(fastener='laces'),
            FastenType(fastener='velcrow'),
            FastenType(fastener='other'),
        ])

        # Shoe.objects.bulk_create([
        #     Shoe(manufacturer=Manufacturer.objects.filter(name="USA").first(),
        #          brand=BrandName.objects.filter(brand='nike').first(),
        #          shoe_type=ShoeType.objects.filter(style='sneaker').first(),
        #          color=ShoeColor.objects.filter(color_name='red').first(),
        #          size=ShoeSize.objects.filter(size='7').first(),
        #          material=ShoeMaterial.objects.filter(material='leather').first(),
        #          fastener=FastenType.objects.filter(fastener='laces').first())
        # ])
