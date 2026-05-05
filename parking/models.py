from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.

plate_validator = RegexValidator(
    regex=r'^[A-Za-z0-9]{6}$',
    message="Plate number must be exactly 6 characters, containing only letters and digits (e.g., 603ZPC)."
)

class ParkingSpace(models.Model):
    space_number = models.IntegerField(unique=True, help_text="Unique number for the parking space")
    vehicle_type = models.CharField(max_length=50, blank=True, null=True, help_text="Type of vehicle (e.g., car, truck, motorcycle)")
    plate_number = models.CharField(max_length=6, blank=True, null=True, validators=[plate_validator], help_text="Vehicle license plate number (exactly 6 characters, letters and digits only, e.g., 603ZPC)")
    owner_name = models.CharField(max_length=100, blank=True, null=True, help_text="Name of the vehicle owner")
    occupancy_status = models.BooleanField(default=False, help_text="True if occupied, False if free")
    entry_time = models.DateTimeField(blank=True, null=True, help_text="Time when vehicle entered")
    exit_time = models.DateTimeField(blank=True, null=True, help_text="Time when vehicle exited")

    def __str__(self):
        status = "Occupied" if self.occupancy_status else "Free"
        return f"Space {self.space_number} - {status}"

    def duration(self):
        if self.entry_time and self.exit_time:
            return self.exit_time - self.entry_time
        elif self.entry_time:
            return timezone.now() - self.entry_time
        return None
