from django.db import models

# Create your models here.


class Admission(models.Model):
    first_name = models.CharField(max_length=11, null=True)
    middle_name = models.CharField(max_length=11, null=True)
    last_name = models.CharField(max_length=11, null=True)
    dob = models.DateField()

    male = 'male'
    female = 'female'
    
    gender_type = [
        ('male', male),
        ('female', female),
    ]
    gender= models.CharField(max_length=10, choices=gender_type, default=female)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=11, null=True)
    expected_admission_session = models.DateField()
    last_class_passed = models.CharField(max_length=11, null=True)
    intended_class = models.CharField(max_length=11, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)


    def __str__ (self):
        return f'{self.first_name} Admission Application'
