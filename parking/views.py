from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ParkingSpace
from .forms import ParkingSpaceForm

# Create your views here.

class ParkingSpaceListView(ListView):
    model = ParkingSpace
    template_name = 'parking/parkingspace_list.html'
    context_object_name = 'parking_spaces'

    def get_queryset(self):
        # Auto-populate if no spaces exist
        if not ParkingSpace.objects.exists():
            self.populate_initial_spaces()
        return ParkingSpace.objects.all()

    def populate_initial_spaces(self):
        """Populate database with initial parking spaces if empty"""
        try:
            spaces_data = [
                {'space_number': i, 'owner_name': '', 'vehicle_type': '', 'plate_number': '', 'occupancy_status': False}
                for i in range(1, 21)
            ]
            for space_data in spaces_data:
                ParkingSpace.objects.create(**space_data)
        except Exception as e:
            # Log error but don't break the app
            print(f"Error populating spaces: {e}")
            pass

class ParkingSpaceDetailView(DetailView):
    model = ParkingSpace
    template_name = 'parking/parkingspace_detail.html'

class ParkingSpaceCreateView(CreateView):
    model = ParkingSpace
    form_class = ParkingSpaceForm
    template_name = 'parking/parkingspace_form.html'
    success_url = reverse_lazy('parking:parkingspace_list')

class ParkingSpaceUpdateView(UpdateView):
    model = ParkingSpace
    form_class = ParkingSpaceForm
    template_name = 'parking/parkingspace_form.html'
    success_url = reverse_lazy('parking:parkingspace_list')

class ParkingSpaceDeleteView(DeleteView):
    model = ParkingSpace
    template_name = 'parking/parkingspace_confirm_delete.html'
    success_url = reverse_lazy('parking:parkingspace_list')
