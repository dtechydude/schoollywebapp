from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from students.models import StudentDetail
from curriculum.models import Standard, Subject

# Create your models here.
class Session(models.Model):
    name = models.CharField(max_length=150)
  
    def __str__ (self):
        return f'{self.name} session'


class Examination(models.Model):
    name = models.CharField(max_length=150, blank=True)
    standard_name = models.ForeignKey(Standard, on_delete=models.CASCADE)
  
    def __str__ (self):
        return f'{self.name} exam'
    


class Result(models.Model):
    student = models.ForeignKey(StudentDetail, on_delete=models.CASCADE, blank=True, null=True, default=None)
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE) 
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateField(null=True)  
    cand_score = models.IntegerField(blank=True) 
    pass_mark =  models.IntegerField( blank=True) 
    remark = models.CharField(max_length=150, blank=True) 
    file = models.FileField(upload_to='result', blank=True)

    def __str__ (self):
        return f'{self.user.username} Result'

    

class PrintResult(models.Model):
    student = models.ForeignKey(StudentDetail, on_delete=models.CASCADE, blank=True, null=True, default=None)
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    exam_year = models.DateField(null=True)
    file = models.FileField(upload_to='result', blank=True, null=False)

    def __str__ (self):    
        return f'{self.student} - {self.session} - {self.exam_year}'
