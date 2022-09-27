from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from curriculum.models import Standard
from students.models import StudentDetail



class Attendance(models.Model):
    student_id = models.ForeignKey(StudentDetail, on_delete=models.CASCADE, blank=True, null=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(null=True)
    status = models.BooleanField(default=False)
    attendance_date = models.DateTimeField(auto_now_add=True)


    def __str__ (self):
        return f'{self.student_id} - { self.date}Attendance'
