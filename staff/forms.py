from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StaffAcademicInfo, StaffProfile


class StaffUpdateForm(forms.ModelForm):

    class Meta:
        model = StaffAcademicInfo
        fields = '__all__'

       # Widget = {'date_employed': forms.DateInput()}

