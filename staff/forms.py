from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StaffProfile


class StaffRegisterForm(forms.ModelForm):

    class Meta:
        model = StaffProfile
        fields = '__all__'

       # Widget = {'date_employed': forms.DateInput()}

