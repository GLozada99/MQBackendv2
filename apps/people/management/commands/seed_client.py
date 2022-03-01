from django.core.management.base import BaseCommand
from apps.people.models import Client
from faker import Faker
from extras.constants import Constants

faker = Faker()


class Command(BaseCommand):
    help = 'Seeds Client table'

    def handle(self, *args, **options):
        for _ in range(Constants.SEEDED_ELEMENTS):
            item = Client(identification=faker.ssn(),
                          first_name=faker.first_name(),
                          last_name=faker.last_name(),
                          birth_date=faker.date(),
                          email=faker.email(),
                          phone_number=f'{faker.country_calling_code()}'
                                       f'{faker.phone_number()}',
                          address=faker.text(max_nb_chars=50))
            item.save()

            self.stdout.write(self.style.SUCCESS(
                f'Successfully created {item}'))
