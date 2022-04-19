from django.shortcuts import get_object_or_404, render, redirect
from staff.models import StaffAcademicInfo, StaffProfile
# from students.models import Mystudents, StudentDetails, StudentProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
#converting html to pdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from students.models import StudentDetail, StudentProfile
from students.forms import StudentUpdateForm, StudentProfileForm
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.http import FileResponse
import csv



# @login_required
@login_required
def studentupdateform(request):
    if request.method == 'POST':
        su_form = StudentUpdateForm(request.POST)
        sa_form = StudentProfileForm(request.POST)
      
        if su_form.is_valid and sa_form.is_valid():
            su_form.save()
            sa_form.save()
            
            messages.success(request, f'Your account has been updated successfully')
            return redirect('profile')
    else:
         su_form = StudentUpdateForm()
         sa_form = StudentDetail()
       
            
    context = {
        'su_form': su_form,
        'sa_form': sa_form,
   
    }

    return render(request, 'students/student_update_form.html', context)




@login_required
def studentlist(request):
    studentlist = StudentDetail.objects.all()
    context = {
        'studentlist' : studentlist

    }
    return render (request, 'students/student_list.html', context)





class StudentListView(ListView):
    model = StudentDetail
    template_name = 'students/main.html'

def student_render_pdf_view(request, *args, **kwargs):    

    pk = kwargs.get('pk')
    
    student = get_object_or_404(StudentDetail, pk=pk)
    template_path = 'students/pdf2.html'
    context = {'student': student}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you want to download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you just want to display
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



# redering pdf function
def render_pdf_view(request):
    template_path = 'students/pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you want to download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you just want to display
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def studentpage(request):

    return render(request, 'students/student_page.html', {})


# @login_required
# def studentlist(request):
#     context = {
#         'studentlist':StudentAcademicInfo.objects.all()
#     }

    
#     return render(request, 'students/student_list.html', {})




# #@login_required
# def studentlist(request):
#     studentlist = Mystudents.objects.all()
#     context = {
#         'studentlist' : studentlist

#    }
#     return render (request, 'students/student_list.html', context)

@login_required
def studentlist(request):
    studentlist = StudentDetail.objects.all()
    context = {
        'studentlist' : studentlist

    }
    return render (request, 'students/student_list.html', context)



# @login_required
# def studentupdateprofile(request):
#     if request.method == 'POST':
        
#         aca_form = StudentUpdateForm(request.POST)
#         if std_form.is_valid():
           
#             std_form.save()
#             messages.success(request, f'Your account has been updated successfully')
#             return redirect('profile')
#     else:
      
#         std_form = StudentUpdateForm

#     context = {
        
#         'std_form': aca_form,
#     }

#     return render(request, 'students/student_update_form.html', context)






# Generate a PDF staff list
def mystudent_pdf(request):
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
    student = StudentDetail.objects.all()

    # Create a blank list
        
    lines = [" Student List Report"]

    for students in student:
        lines.append(""),
        lines.append("Username: " + students.user.username),
        lines.append("Current Class: " + str(students.current_class)),
        lines.append("Class Teacher: " + str(students.class_teacher.user.username)), 
        lines.append("Student Type: " + students.student_type),
        lines.append("-------------------------------------"),


    # loop
    for line in lines:
        textob.textLine(line)
    #fininsh up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    # Return something
    return FileResponse(buf, as_attachment=False, filename='students.pdf')


# Generate a CSV staff list
def mystudent_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename=student.csv'
    
# Create a csv writer
    writer = csv.writer(response)

    student = StudentDetail.objects.all()
    
    # Add column headings to the csv files
    writer.writerow(['Student Name', 'Class Teacher', 'Current Class', 'Student Type'])


    # Loop thru and output
    for students in student:
        writer.writerow([students.user.username, students.current_class, students.class_teacher, students.student_type])
        
    return response
