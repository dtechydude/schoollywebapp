from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import StudentDetail
from staff.models import StaffProfile
from django.views.generic import  ListView
from .models import SchoolCalendar

# Create your views here.
#
class CalendarListView(ListView):
    model = SchoolCalendar
    template_name = 'portal/portal-home.html'
    context_object_name = 'calendar'
    ordering = ['-date_posted']
    paginate_by = 4


@login_required
def portal_home(request):
    student_num = StudentDetail.objects.count()
    num_inclass = StudentDetail.objects.filter(current_class__name='Jss1').count()
    graduated = StudentDetail.objects.filter(student_status='graduated').count()
    dropped = StudentDetail.objects.filter(student_status='dropped').count()
    expelled = StudentDetail.objects.filter(student_status='expelled').count()
    suspended = StudentDetail.objects.filter(student_status='suspended').count()
    active = StudentDetail.objects.filter(student_status='active').count()
    staff_num = StaffProfile.objects.count()
    queryset = SchoolCalendar.objects.all()
    
    context = {
        'student_num': student_num,
        'num_inclass': num_inclass,
        'staff_num': staff_num,
        'graduated': graduated,
        'dropped': dropped,
        'expelled': expelled,
        'suspended': suspended,
        'active': active,
        'queryset': queryset,
    }
    return render(request, 'portal/portal-home.html', context)


