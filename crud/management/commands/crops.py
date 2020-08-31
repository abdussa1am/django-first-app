from crud.models import Crop
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)
        insert_count = Crop.objects.from_csv(r'C:\Users\Abdus Salam\Desktop\django\portfolio\crud\management\commands\crop.csv')
        print("{} records inserted ".format(insert_count))