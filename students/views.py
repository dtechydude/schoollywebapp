from django.shortcuts import get_object_or_404, render, redirect
from staff.models import StaffProfile
from students.models import StudentAcademicInfo, StudentProfile
from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from students.forms import StudentAcademicInfo, StudentProfile



# @login_required
def studentupdateprofile(request):
    if request.method == 'POST':
        su_form = StudentProfile(request.POST)
        sa_form = StudentAcademicInfo(request.POST)
      
        if su_form.is_valid() and sa_form.is_valid():
            su_form.save()
            sa_form.save()
            
            messages.success(request, f'Your account has been updated successfully')
            return redirect('profile')
    else:
        su_form = StudentProfile()
        sa_form = StudentAcademicInfo()
       
            
    context = {
        'su_form': su_form,
        'sa_form': sa_form,
   
    }

    return render(request, 'students/student_profile.html', context)





def studentpage(request):

    return render(request, 'students/student_page.html', {})

@login_required
def studentlist(request):
    student_list = StudentProfile.objects.all()
    context = {
        'studentlist':student_list
    }
    
    return render(request, 'students/student_list.html', context)








