from django import forms
from .models import Attendance


class StudentAttendanceForm(forms.ModelForm):
    
    class Meta:
        model = Attendance
        fields = ['select_class', 'select_student', 'date', 'status']
        widgets = {
            'date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }


   
