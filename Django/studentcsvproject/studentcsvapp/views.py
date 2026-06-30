from django.shortcuts import render,redirect,get_object_or_404
from .models import Department,Student
import csv
from io import TextIOWrapper

# Create your views here.
def home(request):
    return render(request,"home.html")

def show_s(request):
    data=Student.objects.all()
    return render(request,"show_s.html",{"data":data})

def show_d(request):
    data=Department.objects.all()
    return render(request,"show_d.html",{"data":data})

def upload(request):
    if request.method=="POST":
        csv_file=request.FILES['csv_file']
        file=TextIOWrapper(csv_file.file,encoding='utf-8')
        reader=csv.reader(file)
        next(reader)
        for i in reader:
            name=i[0]
            enroll=i[1]
            email=i[2]
            dep_name=i[3]
            department,created=Department.objects.get_or_create(
                dep_name=dep_name,
                hod_name="hod"
            )
            Student.objects.create(name=name,enroll=enroll,email=email,department=department)
        return redirect("shows")
    return render(request,"upload.html")

def delete(request,id):
    d=get_object_or_404(Student,id=id)
    d.delete()
    return redirect("shows")