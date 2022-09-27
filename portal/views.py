from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import StudentDetail
from staff.models import StaffProfile
from django.views.generic import  ListView
from .models import SchoolCalendar
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

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
    
    # Build a paginator with function based view
    queryset = SchoolCalendar.objects.all().order_by("-id")
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 4)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    
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
        'events':events,
    }
    return render(request, 'portal/portal-home.html', context)


