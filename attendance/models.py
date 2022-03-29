from django.db import models

from django.db import models

# Create your models here.


class Attendance(models.Model):
    student_name = models.CharField(max_length=11, null=True)
    date = models.DateField(null=True)
    status = models.CharField(max_length=11, null=True)
    attendance_date = models.DateField(null=True)


    def __str__ (self):
        return f'{self.user.username} Attendance'
