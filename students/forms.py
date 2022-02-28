from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentAcademicInfo, StudentProfile


class StudentProfile(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = '__all__'


class StudentAcademicInfo(forms.ModelForm):

    class Meta:
        model = StudentAcademicInfo
        fields = '__all__'

