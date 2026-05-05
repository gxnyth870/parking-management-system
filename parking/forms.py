from django import forms
from .models import ParkingSpace

class ParkingSpaceForm(forms.ModelForm):
    class Meta:
        model = ParkingSpace
        fields = ['space_number', 'owner_name', 'vehicle_type', 'plate_number', 'occupancy_status', 'entry_time', 'exit_time']
        widgets = {
            'entry_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'datetime-input',
            }),
            'exit_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'datetime-input',
            }),
        }