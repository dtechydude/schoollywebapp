from email.policy import default
from django.db import models

from django.db import models

# Create your models here.


class Attendance(models.Model):
    select_class = models.CharField(max_length=11, null=True)
    select_student = models.CharField(max_length=11, null=True)
    date = models.DateField(null=True)
    status = models.BooleanField(default=False)
    attendance_date = models.DateTimeField(auto_now_add=True)


    def __str__ (self):
        return f'{self.user.username} Attendance'
