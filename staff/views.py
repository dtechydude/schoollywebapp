from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from staff.forms import StaffRegisterForm
from staff.models import StaffProfile
from users.models import Profile
from django.http import HttpResponse
from django.views.generic import DetailView
#for pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# for csv
import csv

# Create your views here.


@login_required
def staffupdateprofile(request):
    if request.method == 'POST':
        
        aca_form = StaffRegisterForm(request.POST)
        if aca_form.is_valid():
           
            aca_form.save()
            messages.success(request, f'New Staff Registered successfully')
            return redirect('staff:staff_detail')
    else:
      
        aca_form = StaffRegisterForm

    context = {
        
        'aca_form': aca_form,
    }

    return render(request, 'staff/staff_register_form.html', context)


@login_required
def stafflist(request):
    context = {
        'stafflist' : StaffProfile.objects.all()

    }
    return render (request, 'staff/staff_list.html', context)



# Generate a PDF staff list
def staff_pdf(request):
    # create Bytestream buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 12)
    # Add some lines of text
    # lines = [
    #     "This is line 1",
    #     "This is line 2",
    #     "This is line31",
    #     "This is line 4",
    # ]
    # Designate the model
    staff = StaffProfile.objects.all()

    # Create a blank list
        
    lines = [" This is the Report of your school"]

    for staffs in staff:
        lines.append(""),
        lines.append("Username: " + staffs.user.username),
        lines.append("Qualification: " + staffs.qualification),
        lines.append("Year: " + staffs.year),
        lines.append("Institution: " + staffs.institution),
        lines.append (staffs.marital_status),
        lines.append("Phone: " + staffs.phone),
        lines.append("========="),


    # loop
    for line in lines:
        textob.textLine(line)
    #fininsh up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    # Return something
    return FileResponse(buf, as_attachment=False, filename='staff.pdf')


# Generate a CSV staff list
def staff_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename=staff.csv'
    
# Create a csv writer
    writer = csv.writer(response)

    staff = StaffProfile.objects.all()
    
    # Add column headings to the csv files
    writer.writerow(['Staff Name', 'Year', 'Phone', 'Institution'])


    # Loop thru and output
    for staffs in staff:
        writer.writerow([staffs.user.username, staffs.year, staffs.phone, staffs.institution])
        
    return response


class StaffDetailView(DetailView):
    template_name = 'staff/staff_details.html'
    # queryset = StaffProfile.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(StaffProfile, id=id_)
   



