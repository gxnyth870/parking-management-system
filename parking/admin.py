from django.contrib import admin
from .models import ParkingSpace

class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = ('space_number', 'owner_name', 'vehicle_type', 'plate_number', 'occupancy_status', 'entry_time')
    list_filter = ('occupancy_status', 'vehicle_type')
    search_fields = ('space_number', 'owner_name', 'plate_number', 'vehicle_type')
    fieldsets = (
        ('Space Information', {
            'fields': ('space_number',)
        }),
        ('Vehicle & Owner', {
            'fields': ('owner_name', 'vehicle_type', 'plate_number')
        }),
        ('Occupancy Status', {
            'fields': ('occupancy_status',)
        }),
        ('Time Tracking', {
            'fields': ('entry_time', 'exit_time')
        }),
    )

admin.site.register(ParkingSpace, ParkingSpaceAdmin)
