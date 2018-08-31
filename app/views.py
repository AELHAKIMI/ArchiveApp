from django.shortcuts import render
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views import generic
from .models import Patient, Service, Dossier

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'all_Patients'

    def get_queryset(self):
        return Patient.objects.all()

class DetailView(generic.DetailView):
    model = Patient
    template_name = 'app/Detail.html'


class PatientCreate(CreateView):
    model = Patient
    fields = ['IndexPatient', 'NomPatient', 'SexePatient', 'NumTelephone', 'AdressePatient']
