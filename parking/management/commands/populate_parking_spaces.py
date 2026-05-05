from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Populate database with initial parking spaces'

    def handle(self, *args, **options):
        try:
            ParkingSpace = apps.get_model('parking', 'ParkingSpace')

            if ParkingSpace.objects.count() == 0:
                spaces_data = [
                    {'space_number': i, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False}
                    for i in range(1, 21)
                ]

                for space_data in spaces_data:
                    ParkingSpace.objects.create(**space_data)

                self.stdout.write(
                    self.style.SUCCESS('Successfully created 20 parking spaces')
                )
            else:
                self.stdout.write(
                    self.style.WARNING('Parking spaces already exist, skipping creation')
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating parking spaces: {str(e)}')
            )
            raise