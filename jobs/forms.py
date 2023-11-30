from django import forms
from .models import Applicant


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'email', 'bio', 'skills', 'resume']
