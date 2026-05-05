import os
import sys
import django
from datetime import datetime

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parking_web.settings')
django.setup()

from parking.models import ParkingSpace

def display_menu():
    print("\nParking Simulator Menu")
    print("1. View all parking spaces")
    print("2. Park a vehicle")
    print("3. Remove a vehicle")
    print("4. View space details")
    print("5. Exit")

def view_spaces():
    spaces = ParkingSpace.objects.all()
    if not spaces:
        print("No parking spaces available.")
        return
    for space in spaces:
        status = "Occupied" if space.occupancy_status else "Free"
        print(f"Space {space.space_number}: {status}")
        if space.entry_time:
            print(f"  Entry: {space.entry_time}")
        if space.exit_time:
            print(f"  Exit: {space.exit_time}")
        if space.duration():
            print(f"  Duration: {space.duration()}")

def park_vehicle():
    space_num = int(input("Enter space number: "))
    try:
        space = ParkingSpace.objects.get(space_number=space_num)
        if space.occupancy_status:
            print("Space is already occupied.")
            return
        vehicle_type = input("Enter vehicle type: ")
        plate_number = input("Enter plate number (6 characters, letters and digits only, e.g., 603ZPC): ")
        space.vehicle_type = vehicle_type
        space.plate_number = plate_number
        space.occupancy_status = True
        space.entry_time = datetime.now()
        space.save()
        print("Vehicle parked successfully.")
    except ParkingSpace.DoesNotExist:
        print("Space does not exist.")

def remove_vehicle():
    space_num = int(input("Enter space number: "))
    try:
        space = ParkingSpace.objects.get(space_number=space_num)
        if not space.occupancy_status:
            print("Space is already free.")
            return
        space.occupancy_status = False
        space.exit_time = datetime.now()
        space.save()
        print("Vehicle removed successfully.")
        if space.duration():
            print(f"Parking duration: {space.duration()}")
    except ParkingSpace.DoesNotExist:
        print("Space does not exist.")

def view_details():
    space_num = int(input("Enter space number: "))
    try:
        space = ParkingSpace.objects.get(space_number=space_num)
        print(f"Space {space.space_number}")
        print(f"Status: {'Occupied' if space.occupancy_status else 'Free'}")
        print(f"Vehicle Type: {space.vehicle_type or 'N/A'}")
        print(f"Plate Number: {space.plate_number or 'N/A'}")
        print(f"Entry Time: {space.entry_time or 'N/A'}")
        print(f"Exit Time: {space.exit_time or 'N/A'}")
        if space.duration():
            print(f"Duration: {space.duration()}")
    except ParkingSpace.DoesNotExist:
        print("Space does not exist.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_spaces()
        elif choice == '2':
            park_vehicle()
        elif choice == '3':
            remove_vehicle()
        elif choice == '4':
            view_details()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()