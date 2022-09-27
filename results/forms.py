from django import forms
from results.models import Result, PrintResult
#from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


class ResultUploadForm(forms.ModelForm):
        
        class Meta:
            model = Result
            fields = '__all__'

            widgets = {
            'exam_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }

           



class PrintResultForm(forms.ModelForm):
        
        class Meta:
            model = PrintResult
            fields =  '__all__'

            widgets = {
            'exam_year': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }