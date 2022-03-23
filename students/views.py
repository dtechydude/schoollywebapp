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






