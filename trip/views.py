from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.
class TripListView(ListView):
    template_name = 'trip/index.html'  # Hauptseite

