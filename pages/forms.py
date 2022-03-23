from django import forms
from .models import Admission



class EnrollmentForm(forms.ModelForm):
    
    class Meta:
        model = Admission
        fields = '__all__'

       # Widget = {'date_employed': forms.DateInput()}
