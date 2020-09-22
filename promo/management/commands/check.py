from django.core.management.base import BaseCommand
import json


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('promo', nargs=1, type=str, help='promocode')

    def handle(self, *args, **options):
        file_name = 'promotion.json'
        for arg in options['promo']:
            code = arg
        #self.stdout.write(options['promo'])
        with open(file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            if (code not in str(data)):
                self.stdout.write('Код не существует')
            else:
                for el in data:
                    for f_code in el['promo']:
                        if f_code == code:
                            group = str(el['name'])
                            self.stdout.write(f'Код существует, группа {group}')