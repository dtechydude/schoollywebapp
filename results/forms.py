from django import forms
from results.models import PrintResult


class ResultUploadForm(forms.ModelForm):
        
        class Meta:
            model = PrintResult
            fields = '__all__'