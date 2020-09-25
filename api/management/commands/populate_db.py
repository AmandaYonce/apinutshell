from django.core.management.base import BaseCommand
from api.models import ShoeType, ShoeColor


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

        