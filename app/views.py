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

class PatientDetailView(generic.DetailView):
    model = Patient
    template_name = 'app/Patient/Detail_Patient.html'


class PatientCreateView(CreateView):
    model = Patient
    fields = ['IndexPatient', 'NomPatient', 'SexePatient', 'NumTelephone', 'AdressePatient']

class DossierCreateView(CreateView):
    model = Dossier
    fields = '__all__'

class DossierDetailView(generic.DetailView):
    model = Dossier
    template_name = 'app/Dossier/detail_Dossier.html'

class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'app/Service/detail_Service.html'

class ServiceCreateView(CreateView):
    model = Service   
    fields = '__all__'
