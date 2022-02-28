from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from results.forms import ResultUploadForm
from django.contrib import messages
from results.models import PrintResult, Result

# Create your views here.

@login_required
def printresult(request):
    result = PrintResult.objects.all()
    context = {
        'result':result
    }
    
    return render(request, 'results/print_result.html', context)



@login_required
def uploadresult(request):
    if request.method == 'POST':
        upload_form = ResultUploadForm(request.POST)
        
        if upload_form.is_valid():
             upload_form.save()
             messages.success(request, f'The Result has been uploaded successfully')
             return redirect('studentpage')
        
        else:
            upload_form = ResultUploadForm()
        
        context ={
            'upload_form' : upload_form,
        }
        return render(request, 'results/upload_result_form.html', context)

