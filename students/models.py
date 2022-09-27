from django.db import models
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from curriculum.models import Standard
from django.urls import reverse
from staff.models import StaffProfile


# Create your models here.

class StudentDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_code = models.CharField(max_length=20, blank=True, default='None')  
    current_class = models.ForeignKey(Standard, on_delete=models.CASCADE, default='jss1')
    class_teacher = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)

    day_student = 'day_student'
    boarder = 'boarder'

    student_types = [
        (day_student, 'day_student'),
        (boarder, 'boarder'),

    ]

    student_type = models.CharField(max_length=15, choices=student_types, default=day_student)

    dob = models.DateField(blank=True, null=True)
    # class_on_admission = models.ForeignKey(Standard, on_delete=models.CASCADE)
    date_admitted = models.DateField(null=True)
    # class_on_admission = models.CharField(max_length=50, blank=True, null=True, default=None)
    class_on_admission = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='studentdetails', verbose_name='class_on_admission') 
    # parent details here..
    parent_name = models.CharField(max_length=150, blank=True)  
    parent_address = models.TextField(max_length=150, blank=True)  
    parent_phone = models.CharField(max_length=15, blank=True, null=True)
    parent_email = models.CharField(max_length=15, blank=True, null=True)

    father = 'father'
    mother = 'mother'
    sister = 'sister'
    brother = 'brother'
    other = 'other'

    relationship = [
        (father, 'father'),
        (mother, 'mother'),
        (sister, 'sister'),
        (brother, 'brother'),
        (other, 'other'),  

    ]

    relationship = models.CharField(max_length=15, choices=relationship, default=mother)
    
    active = 'active'
    graduated = 'graduated'
    dropped = 'dropped'
    expelled = 'expelled'

    student_status = [
        (active, 'active'),
        (graduated, 'graduated'),
        (dropped, 'dropped'),
        (expelled, 'expelled'),

    ]

    student_status = models.CharField(max_length=15, choices=student_status, default=active)

#this function returns the profile name in the admin panel profile table
    def __str__ (self):
        return f'{self.user.username} StudentProfile'


    def get_absolute_url(self):
        return reverse('students:students-detail', kwargs={'id':self.id})





# Use for testing API call
class Mystudents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=150, blank=True)  
    year = models.CharField(max_length=150, blank=True)   
    institution = models.CharField(max_length=150, blank=True)
    professional_body = models.CharField(max_length=150, blank=True)  
    academic = models.CharField(max_length=150, blank=True)  

    def __str__ (self):
        return f'{self.user.username} StudentAcademicInfo'



# Used on client's website
class AdmissionApplication(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.CharField(max_length=150, blank=False, null=False)
    phone = models.CharField(max_length=150, blank=False, null=False)
    city = models.CharField(max_length=150, blank=False, null=False)
    last_class = models.CharField(max_length=150, blank=False, null=False)
    new_class = models.CharField(max_length=150, blank=False, null=False)
    application_date = models.DateField(auto_now=True)
    

    def __str__(self):
        return f'{self.name} - {self.application_date}'
