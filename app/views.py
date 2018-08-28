from django.shortcuts import render
from django.views import generic
from .models import Patient, Service, Dossier

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Patient.objects.all()

class DetailView(generic.DetailView):
    model = Patient
    template_name = 'Detail.html'
    