from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
#

@login_required
def portal_home(request):
    return render(request, 'portal/portal-home.html')

@login_required
def student_list(request):
    return render(request, 'portal/student_list.html')


@login_required
def staff_list(request):
    return render(request, 'portal/staff-list.html')

@login_required
def elearning_list(request):
    return render(request, 'portal/elearning_class.html')