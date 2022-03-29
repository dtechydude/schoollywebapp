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


def test(request):
    return render(request, 'demoschool/test.html')