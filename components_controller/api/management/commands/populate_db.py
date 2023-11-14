"""# your_app/management/commands/populate_db.py
import json
from django.core.management.base import BaseCommand
from components_controller.api.models import Game, Info, MinimumRequirements, RecommendedRequirements
import requests


class Command(BaseCommand):
    help = 'Populate the database with data from an API'

    def handle(self, *args, **options):
        API_BASE_URL = 'http://plutone00100.pythonanywhere.com/api/v1/'
        API_KEY = 'cf7c9541c2b477a00cbe2549cda1b5c118c75f7f7a2448eebd831611'
        headers = {'x-api-key': API_KEY}
        # Fetch data from the API
        url = f'{API_BASE_URL}games'
        response = requests.get(url, headers=headers)
        return response.json()

    for d in handle():
        print(d)

        # Iterate over the data and create/update records in the database
        for game_data in data:
            info_data = game_data.get('info', {})
            min_req_data = game_data.get('minimum_requirements', {})
            rec_req_data = game_data.get('recommended_requirements', {})

            info, _ = Info.objects.get_or_create(
                name=info_data.get('name'),
                defaults={
                    'description': info_data.get('description', ''),
                    'developer': info_data.get('developer', ''),
                }
            )

            min_req, _ = MinimumRequirements.objects.get_or_create(
                OS_min=min_req_data.get('OS_min', ''),
                defaults={
                    'cpu_min': min_req_data.get('cpu_min', ''),
                    'gpu_min': min_req_data.get('gpu_min', ''),
                    'ram_min': min_req_data.get('ram_min', 0),
                    'storage_min': min_req_data.get('storage_min', 0.0),
                }
            )

            rec_req, _ = RecommendedRequirements.objects.get_or_create(
                OS_rec=rec_req_data.get('OS_rec', ''),
                defaults={
                    'cpu_rec': rec_req_data.get('cpu_rec', ''),
                    'gpu_rec': rec_req_data.get('gpu_rec', ''),
                    'ram_rec': rec_req_data.get('ram_rec', 0),
                    'storage_rec': rec_req_data.get('storage_rec', 0.0),
                }
            )

            game, created = Game.objects.get_or_create(
                id=game_data.get('id'),
                defaults={
                    'info': info,
                    'minimum_requirements': min_req,
                    'recommended_requirements': rec_req,
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Game "{game}" created'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Game "{game}" updated'))
"""