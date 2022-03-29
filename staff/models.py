from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

import datetime


# Create your models here.


class StaffCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    marital_status = models.BooleanField(blank=True, null=True)
    phone = models.CharField(max_length=11, null=True)
    staff_type = models.OneToOneField(StaffCategory, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    next_of_kin = models.CharField(max_length=150, blank=True)  
    next_of_kin_address = models.CharField(max_length=150, blank=True)  
    next_of_kin_phone = models.CharField(max_length=150, blank=True) 
    date_employed = models.DateField(null=True)
    


#this function returns the profile name in the admin panel profile table
    def __str__ (self):
        return f'{self.user.username} Staff Profile'


class StaffAcademicInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=150, blank=True)  
    year = models.CharField(max_length=150, blank=True)   
    institution = models.CharField(max_length=150, blank=True)
    professional_body = models.CharField(max_length=150, blank=True)  
    academic = models.CharField(max_length=150, blank=True)  

    marital_status = models.BooleanField(blank=True, null=True)
    phone = models.CharField(max_length=11, null=True)
    staff_type = models.OneToOneField(StaffCategory, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    next_of_kin = models.CharField(max_length=150, blank=True)  
    next_of_kin_address = models.CharField(max_length=150, blank=True)  
    next_of_kin_phone = models.CharField(max_length=150, blank=True) 
    date_employed = models.DateField(null=True)



#this function returns the profile name in the admin panel profile table
    def __str__ (self):
        return f'{self.user.username} StaffAcademicInfo'