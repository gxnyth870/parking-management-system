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
