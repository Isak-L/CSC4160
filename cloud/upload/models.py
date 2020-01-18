from django.db import models
import uuid

# Create your models here.

class Patient(models.Model):
    pID         = models.CharField(max_length = 15, primary_key=True)
    pFName      = models.CharField(max_length = 30,  blank=True, null=True)
    pLName      = models.CharField(max_length = 30,  blank=True, null=True)
    pGender     = models.CharField(max_length = 10,  blank=True, null=True)
    pRace       = models.CharField(max_length = 20,  blank=True, null=True)
    pEthnicity  = models.CharField(max_length = 20,  blank=True, null=True)
    pStatus     = models.CharField(max_length = 5,   blank=True, null=False)
    pRemark     = models.CharField(max_length = 255, blank=True, null=True)
    pAge        = models.IntegerField(blank=True, null=False)
    pImage      = models.URLField()
    resultImg   = models.URLField(null=True)
    dID         = models.ForeignKey('login.Doctor', on_delete = models.CASCADE)

    def __str__(self):
        return self.pID

