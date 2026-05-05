from django.urls import path
from . import views

app_name = 'parking'

urlpatterns = [
    path('', views.ParkingSpaceListView.as_view(), name='parkingspace_list'),
    path('<int:pk>/', views.ParkingSpaceDetailView.as_view(), name='parkingspace_detail'),
    path('create/', views.ParkingSpaceCreateView.as_view(), name='parkingspace_create'),
    path('<int:pk>/update/', views.ParkingSpaceUpdateView.as_view(), name='parkingspace_update'),
    path('<int:pk>/delete/', views.ParkingSpaceDeleteView.as_view(), name='parkingspace_delete'),
]