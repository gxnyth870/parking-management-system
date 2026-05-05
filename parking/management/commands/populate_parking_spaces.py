from django.core.management.base import BaseCommand
from parking.models import ParkingSpace

class Command(BaseCommand):
    help = 'Populate database with initial parking spaces'

    def handle(self, *args, **options):
        if ParkingSpace.objects.count() == 0:
            spaces_data = [
                {'space_number': 1, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 2, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 3, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 4, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 5, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 6, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 7, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 8, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 9, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 10, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 11, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 12, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 13, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 14, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 15, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 16, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 17, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 18, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 19, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
                {'space_number': 20, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False},
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