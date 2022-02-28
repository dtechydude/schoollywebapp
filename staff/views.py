from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from staff.forms import StaffUpdateForm
from staff.models import StaffAcademicInfo, StaffProfile
from users.models import Profile

# Create your views here.


@login_required
def staffupdateprofile(request):
    if request.method == 'POST':
        
        aca_form = StaffUpdateForm(request.POST)
        if aca_form.is_valid():
           
            aca_form.save()
            messages.success(request, f'Your account has been updated successfully')
            return redirect('profile')
    else:
      
        aca_form = StaffUpdateForm

    context = {
        
        'aca_form': aca_form,
    }

    return render(request, 'staff/staff_profile.html', context)


@login_required
def stafflist(request):
    context = {
        'stafflist' : StaffAcademicInfo.objects.all()

    }
    return render (request, 'staff/staff_list.html', context)



