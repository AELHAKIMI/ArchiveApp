from django.db import models
from django.urls import reverse

# Create your models here.


class Patient(models.Model):
    IndexPatient = models.CharField(
        max_length=12, primary_key=True, verbose_name='Index Patient')
    NomPatient = models.CharField(max_length=250, verbose_name='Nom')
    SexePatient = models.CharField(max_length=32, verbose_name='Sexe')
    NumTelephone = models.CharField(
        max_length=32, verbose_name='Numero telephone')
    AdressePatient = models.CharField(max_length=250, verbose_name='Adresse')

    class Meta:
        verbose_name = 'Patient'

    def __str__(self):
        return self.IndexPatient + " - " + self.NomPatient

    def get_absolute_url(self):
        return reverse('detail-Patient', kwargs={'pk': self.pk})


class Service(models.Model):
    CodeService = models.CharField(max_length=16, unique=True, verbose_name='Code Service')
    NomService = models.CharField(max_length=250, verbose_name='Description')

    class Meta:
        verbose_name = 'Service'

    def __str__(self):
        return self.NomService

    def get_absolute_url(self):
        return reverse('detail-service', kwargs={'pk': self.pk})


class Dossier(models.Model):
    NumeroDossier = models.CharField(max_length=32, verbose_name='Numero Dossier')
    IndexPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Index Patient')
    Service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Code Service')

    verbose_name = 'Dossier'

    def __str__(self):
        return self.NumeroDossier + " - " + str(self.IndexPatient)

    def get_absolute_url(self):
        return reverse('detail-dossier', kwargs={'pk': self.pk})
 