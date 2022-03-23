from django import forms
from .models import Attendance


class StudentAttendanceForm(forms.ModelForm):
    
    class Meta:
        model = Attendance
        fields = '__all__'

   
