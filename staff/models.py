from email.policy import default
from django.urls import reverse
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
    
    married = 'married'
    single = 'single'
    select = 'select'

    marital_status = [
        (married, 'married'),
        (single, 'single'),
        (select, 'select'),
    ]

    marital_status = models.CharField(max_length=15, choices=marital_status, default=select)
    phone = models.CharField(max_length=11, null=True)
    cat_name = models.ForeignKey(StaffCategory, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    date_employed = models.DateField(null=True)

    qualification = models.CharField(max_length=150, blank=True)  
    year = models.DateField()   
    institution = models.CharField(max_length=150, blank=True)
    professional_body = models.CharField(max_length=150, blank=True)  

    guarantor_name = models.CharField(max_length=150, blank=True) 
    guarantor_phone = models.CharField(max_length=150, blank=True) 
    guarantor_email = models.CharField(max_length=150, blank=True)

    next_of_kin_name = models.CharField(max_length=150, blank=True)  
    next_of_kin_address = models.CharField(max_length=150, blank=True)  
    next_of_kin_phone = models.CharField(max_length=150, blank=True) 
    is_active = models.BooleanField(default=True)
    


#this function returns the profile name in the admin panel profile table
    def __str__ (self):
        return f'{self.user.username}'


    def get_absolute_url(self):
        return reverse('staff:staff_detail', kwargs={'id':self.id})



# class StaffAcademicInfo(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     staff_cat = models.ForeignKey(StaffCategory, on_delete=models.CASCADE, blank=True, null=True)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
#     date_employed = models.DateField()
    
#     qualification = models.CharField(max_length=150, blank=True)  
#     year = models.DateField()   
#     institution = models.CharField(max_length=150, blank=True)
#     professional_body = models.CharField(max_length=150, blank=True)  

#     married = 'married'
#     single = 'single'
#     select = 'select'

#     marital_status = [
#         (married, 'married'),
#         (single, 'single'),
#         (select, 'select'),
#     ]
    
#     marital_status = models.CharField(max_length=15, choices=marital_status, default=select)  
#     phone = models.CharField(max_length=11, null=True)  

#     guarantor_name = models.CharField(max_length=150, blank=True) 
#     guarantor_phone = models.CharField(max_length=150, blank=True) 
#     guarantor_email = models.CharField(max_length=150, blank=True)

#     next_of_kin_name = models.CharField(max_length=150, blank=True)  
#     next_of_kin_address = models.CharField(max_length=150, blank=True)  
#     next_of_kin_phone = models.CharField(max_length=150, blank=True) 


# #this function returns the profile name in the admin panel profile table
#     def __str__ (self):
#         return f'{self.user.username} StaffAcademicInfo'