from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'pID',    
            'pFName',
            'pLName',
            'pGender',
            'pRace',
            'pEthnicity',
            'pStatus',
            'pRemark',
            'pAge',
            'pImage'

        ]

class PForm(forms.Form):
    pID           = forms.CharField(),
    pFName        = forms.CharField(),
    pLName        = forms.CharField(),
    pGender       = forms.CharField(),
    pRace         = forms.CharField(),
    pEthnicity    = forms.CharField(),
    pStatus       = forms.CharField(),
    pRemark       = forms.CharField(),
    pAge          = forms.IntegerField(),
    pImage        = forms.URLField()
