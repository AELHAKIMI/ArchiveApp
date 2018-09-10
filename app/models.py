from django.db import models
import datetime
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




YEAR_CHOICES = []
for r in range(1970, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Dossier(models.Model):
    NumeroDossier = models.IntegerField(verbose_name='Numero Dossier')
    AnneeDossier = models.IntegerField(('Annee'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    IndexPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Index Patient')
    Service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Code Service')

    class Meta:        
        verbose_name = 'Dossier'
        verbose_name_plural = 'Dossiers'
        unique_together = ('NumeroDossier', 'AnneeDossier')    

    def __str__(self):
        return str(self.NumeroDossier) + "/" +str(self.AnneeDossier) + " - " + str(self.IndexPatient)

    def get_absolute_url(self):
        return reverse('detail-dossier', kwargs={'pk': self.pk})
    

class DossierDocument(models.Model):
    NumeroDossier = models.ForeignKey(Dossier, on_delete= models.CASCADE, verbose_name= 'Numero Dossier')
    Title = models.CharField(max_length=250, verbose_name= 'Titre')
    Document = models.FileField()
    Description = models.CharField(max_length=1000, verbose_name='Description')

    def get_absolute_url(self):
        return reverse('detail-document', kwargs={'pk': self.pk})

 