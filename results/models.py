from django.db import models
from django.contrib.auth.models import User

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
    exam_date = models.CharField(max_length=150, blank=True)  
    subject_name = models.CharField(max_length=150, blank=True)  
    cand_score = models.CharField(max_length=150, blank=True) 
    pass_mark =  models.CharField(max_length=150, blank=True) 
    remark = models.CharField(max_length=150, blank=True) 

    def __str__ (self):
        return f'{self.user.username} Result'

    

class PrintResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE)
    session = models.CharField(max_length=150, blank=True)
    file = models.CharField(max_length=200, blank=True)

    def __str__ (self):
        return f'{self.user.username} - {self.session} '

   