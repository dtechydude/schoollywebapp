from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import StudentDetail

# Create your views here.
#

@login_required
def portal_home(request):
    student_num = StudentDetail.objects.count()
    num_inclass = StudentDetail.objects.filter(current_class__name='Jss1').count()
    
    context = {
        'student_num': student_num,
        'num_inclass': num_inclass
    }
    return render(request, 'portal/portal-home.html', context)

@login_required
def student_list(request):
    studentlist = StudentDetail.objects.all()
    context = {
        'studentlist' : studentlist

    }
    return render (request, 'portal/student_list.html', context)


@login_required
def staff_list(request):
    return render(request, 'portal/staff-list.html')

@login_required
def elearning_list(request):
    return render(request, 'portal/elearning_class.html')