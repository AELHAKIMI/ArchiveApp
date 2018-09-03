from django import forms
from django.forms import ModelForm
from .models import Patient, Service, Dossier


class PatientForm(forms.Form):
    model = Patient
    fields = '__all__'

    class Meta:
