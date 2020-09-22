from django.core.management.base import BaseCommand
from typing import NoReturn, List
#import collections
import json
import secrets
import os

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('amount', nargs=1, type=str, help='Amount')
        parser.add_argument('name', nargs=1, type=str, help='Name')

    def handle(self, *args, **options):
        def get_args(options):
            for arg in options['amount']:
                amount = str(arg.split('=')[1])
                #self.stdout.write(amount)
            for arg in options['name']:
                name = str(arg.split('=')[1])
            return amount, name
            #return out
        amount, name = get_args(options)

        def get_all_promos(file_name: str) -> List:
            """
            Function which find all promocodes in file
            """
            codes =[]
            with open(file_name, 'r') as json_file:
                data = json.load(json_file)
                for element in data:
                    for code in element['promo']:
                        codes.append(code)
            return codes

        def write_in_json(filename: str) -> NoReturn:
            """
            Function will create file and write promo
            """
            file_name = 'promotion.json'
            promo_len = 8
            if os.path.isfile(file_name):
                with open(file_name, 'a+', encoding='utf-8') as json_file:
                    prev_codes = get_all_promos(file_name)
                    json_file.seek(json_file.seek(0, os.SEEK_END)-1)
                    json_file.truncate()
                    json_file.write(',')
                    codes = []
                    for i in range(int(amount)):
                        while True:
                            new_code = ''.join(secrets.choice('0123456789ABCDEFGHJKLMNPQRSTVWXYZ') for i in range(promo_len))
                            if (new_code not in prev_codes) and (new_code not in codes):
                                codes.append(new_code)
                                break
                    data_dict={'name': name, 'promo': list(codes)}
                    json.dump(data_dict, json_file, ensure_ascii=False, indent=4)
                    json_file.write(']')
            else:
                with open(file_name, 'w', encoding='utf-8') as json_file:
                    array = []
                    codes = {''.join(secrets.choice('0123456789ABCDEFGHJKLMNPQRSTVWXYZ') for i in range(promo_len)) for i in range(int(amount))}
                    array.append({'name': name, 'promo': list(codes)})
                    json.dump(array, json_file, ensure_ascii=False, indent=4)

        write_in_json('promotion.json')