from django.shortcuts import render

# Create your views here.


def demoschool(request):
    return render(request, 'demoschool/index.html')

def allcourses(request):
    return render(request, 'demoschool/all_courses.html')

def school_gallery(request):
    return render(request, 'demoschool/school_gallery.html')

def contact_us(request):
    return render(request, 'demoschool/contact_us.html')

def about_us(request):
    return render(request, 'demoschool/about_us.html')

def admission(request):
    return render(request, 'demoschool/admission.html')


def test(request):
    return render(request, 'demoschool/test.html')

def admin(request):
    return render(request, 'demoschool/admin-login.html')

def infoblog(request):
    return render(request, 'demoschool/infoblog.html')

def academics(request):
    return render(request, 'demoschool/academics.html')

def school_gallery(request):
    return render(request, 'demoschool/school_gallery.html')


