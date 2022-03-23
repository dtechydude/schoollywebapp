from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from attendance.models import StudentDetail, StudentProfile
from attendance.forms import StudentAttendanceForm


# Create your views here.


@login_required
def student_attendance(request):
    if request.method == 'POST':
        attd_form = StudentAttendanceForm(request.POST)
      
        if attd_form.is_valid():
            attd_form.save()
            
            messages.success(request, f'Your account has been updated successfully')
            return redirect('profile')
    else:
         attd_form = StudentAttendanceForm()
    
       
            
    context = {
        'attd_form': attd_form,
       
   
    }

    return render(request, 'students/student_attendance_form.html', context)