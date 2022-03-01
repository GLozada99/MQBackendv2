import tempfile
from django.core.management.base import BaseCommand
from apps.products.models import Product
from faker import Faker
from extras.constants import Constants

faker = Faker()


class Command(BaseCommand):
    help = 'Seeds Product table'

    def handle(self, *args, **options):
        for _ in range(Constants.SEEDED_ELEMENTS):
            pic = tempfile.NamedTemporaryFile(suffix=".jpg").name
            item = Product(name=f'{faker.word().capitalize()} {faker.word()}',
                           description=faker.text(max_nb_chars=50),
                           picture=pic,
                           price=faker.pydecimal(
                               left_digits=2, right_digits=2, min_value=0.01),
                           availability=faker.pyint(min_value=10, max_value=50)
                           )
            item.save()

            self.stdout.write(self.style.SUCCESS(
                f'Successfully created {item}'))
