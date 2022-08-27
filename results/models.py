from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.
class Examination(models.Model):
    name = models.CharField(max_length=150, blank=True)
    category = models.CharField(max_length=150, blank=True)  #test, exam, quiz
  
    def __str__ (self):
        return f'{self.name} Examination'
    


class Result(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE)
    session = models.CharField(max_length=150, blank=True) 
    standard =models.CharField(max_length=150, blank=True) 
    exam_date = models.DateField(null=True)  
    subject_name = models.CharField(max_length=150, blank=True)  
    cand_score = models.CharField(max_length=150, blank=True) 
    pass_mark =  models.CharField(max_length=150, blank=True) 
    remark = models.CharField(max_length=150, blank=True) 

    def __str__ (self):
        return f'{self.user.username} Result'

    

class PrintResult(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE)
    session = models.CharField(max_length=150, blank=True)
    exam_year = models.DateField(null=True)
    file = models.FileField(upload_to='result', blank=True)

    def __str__ (self):    
        return f'{self.user.username} - {self.session} '

   