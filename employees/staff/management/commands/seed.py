import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from employees.staff.models import Staff


class Command(BaseCommand):
    help = 'Populate the database with random data'

    def boss_multiplier(self, *args, **options):
        x = 1
        while True:
            if x**4 + x**3 + x**2 + x + 1 >= 50000:
                break
            x += 1
        print(x)


    def handle(self, *args, **options):
        seeder = Seed.seeder()
        roles = [x[0] for x in Staff.ROLES]
        i = 1
        for role in roles:
            seeder_data = {
                'full_name': lambda x: seeder.faker.name(),
                'role': role,
                'date_joined': lambda x: seeder.faker.date_this_century(),
                'salary': lambda x: seeder.faker.random_int(min=2000, max=100000),
            }
            if role != roles[0]:
                seeder_data['boss'] = random.choice(Staff.objects.filter(role=boss).all())
            seeder.add_entity(Staff, i, seeder_data)
            seeder.execute()

            boss = role
            quantity -= i
            i = random.randint(1, quantity)
        self.stdout.write(self.style.SUCCESS('Successfully populated database with random data'))
