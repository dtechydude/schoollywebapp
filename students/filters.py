import django_filters
from .models import StudentDetail
from django.contrib.auth.models import User

class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = StudentDetail
        fields = {'current_class': ['exact']}
        

