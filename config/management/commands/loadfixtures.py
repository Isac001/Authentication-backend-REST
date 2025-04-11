from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):

    help = "Load fixtures from the fixtures directory"

    def add_arguments(self, parser):

        parser.add_argument(
            '--path',
            type=str,
            default='config/fixtures/',
            help='Path to the fixtures directory'
        )

    def handle(self, *args, **options):

        fixtures_path = options['path']

        fixtures_file = []

        if not os.path.exists(fixtures_path):
            self.stdout.write(self.style.ERROR(f'Path {fixtures_path} does not exist.\n'))
            return
        
        for file_name in os.listdir(fixtures_path):

            if file_name.endswith('.json'):
                fixtures_file.append(os.path.join(fixtures_path, file_name))

        if not fixtures_file:

            self.stdout.write(self.style.WARNING(f'No fixtures found in {fixtures_path}.\n'))
            return
        
        self.stdout.write(f"Loading fixtures from {fixtures_path}...\n")

        for fixture in fixtures_file:

            self.stdout.write(f"Loading fixture {fixture}...\n")
            call_command('loaddata', fixture)

        self.stdout.write(self.style.SUCCESS(f"Fixtures loaded successfully from {fixtures_path}.\n"))
