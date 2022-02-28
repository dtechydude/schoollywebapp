from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from curriculum.models import Standard

from staff.models import StaffProfile


# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    class_on_admission = models.ForeignKey(Standard, on_delete=models.CASCADE)
    date_admitted = models.DateField() 
    parent_name = models.CharField(max_length=150, blank=True)  
    parent_address = models.TextField(max_length=150, blank=True)  
    parent_phone = models.CharField(max_length=15, blank=True, null=True) 
    relationship = models.CharField(max_length=30, blank=True)
   
    


#this function returns the profile name in the admin panel profile table
    def __str__ (self):
        return f'{self.user.username} - StudentProfile'


class StudentAcademicInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_class = models.ForeignKey(Standard, on_delete=models.CASCADE, default='jss1')
    class_teacher = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)

    day_student = 'day_student'
    boarder = 'boarder'

    student_types = [
        (day_student, 'day_student'),
        (boarder, 'boarder'),

    ]

    student_type = models.CharField(max_length=15, choices=student_types, default=day_student)
  



#this function returns the profile name in the admin panel profile table
    def __str__ (self):
        return f'{self.user.username} StudentAcademicInfo'