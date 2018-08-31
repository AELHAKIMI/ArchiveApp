from django.db import models
from django.urls import reverse

# Create your models here.


class Patient(models.Model):
    IndexPatient    = models.CharField(max_length = 12, primary_key = True)
    NomPatient      = models.CharField(max_length = 250)
    SexePatient     = models.CharField(max_length = 32)
    NumTelephone    = models.CharField(max_length = 32)
    AdressePatient  = models.CharField(max_length = 250)

    def __str__(self):
        return self.IndexPatient + " - " + self.NomPatient

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Service(models.Model):
    CodeService = models.CharField(max_length = 16, primary_key = True)
    NomService  = models.CharField(max_length = 250)

    def __str__(self):
        return self.NomService
    

class Dossier(models.Model):
    NumeroDossier   = models.CharField(max_length = 32, primary_key = True)
    IndexPatient    = models.ForeignKey(Patient, on_delete = models.CASCADE)
    Service         = models.ForeignKey(Service, on_delete = models.CASCADE)

    def __str__(self):
        return self.NumeroDossier + " - " +  str(self.IndexPatient)
