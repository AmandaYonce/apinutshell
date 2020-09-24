from django.core.management.base import BaseCommand
from api.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'some help string'

    def add_arguments(self, parser):
        parser.add_argument('populate_db', nargs='+', type=str)

    def _populate(self, *args, **options):
        pass

    def handle(self, *args, **options):
        self._populate()