from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from attendance.models import Attendance
from attendance.forms import StudentAttendanceForm


# Create your views here.


@login_required
def student_attendance(request):
    if request.method == 'POST':
        attd_form = StudentAttendanceForm(request.POST)
      
        if attd_form.is_valid():
            attd_form.save()
            
            messages.success(request, f'Attendance taken. exit or enter another')
            return redirect('attendance:attendance_form')
    else:
         attd_form = StudentAttendanceForm()
    
       
            
    context = {
        'attd_form': attd_form,
       
   
    }

    return render(request, 'attendance/take-attendance.html', context)

@login_required
def attendance_view(request):
    context = {
        'attendance' :Attendance.objects.all()
    }
    return render(request, 'attendance/attendance_view.html', context)
