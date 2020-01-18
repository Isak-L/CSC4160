from django.db import models

# Create your models here.
class Doctor(models.Model):
    dID         = models.CharField(max_length = 15,  primary_key=True)
    dAccount    = models.CharField(max_length = 15,  blank=True, null=False)
    dPassword   = models.CharField(max_length = 255, blank=True, null=False) 

    def __str__(self):
        return self.dID