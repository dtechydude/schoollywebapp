from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Mystudents, StudentDetail


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = Mystudents
        fields = '__all__'


class StudentUpdateForm(forms.ModelForm):

    class Meta:
        model = StudentDetail
        fields = '__all__'

