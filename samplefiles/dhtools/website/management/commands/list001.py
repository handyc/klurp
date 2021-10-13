from django.core.management.base import BaseCommand
from demoapp.models import Digitiser

class Command(BaseCommand):
    help = 'Prints the titles of all Posts'

    def add_arguments(self, parser):
        parser.add_argument('witness_choice', nargs='+', type=str)

    def handle(self, *args, **options):
        for a in Digitiser.objects.all():
            print(a.name)



