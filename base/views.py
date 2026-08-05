from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        course=request.POST['course']
        image=request.FILES.get('pic')
        if  not image:
            image='default.webp'
        Student.objects.create(
            name=name,
            course=course,
            simages=image
        )
    data=Student.objects.all()
    return render(request,'home.html',{'data':data})