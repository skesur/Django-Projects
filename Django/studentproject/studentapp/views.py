from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
# Create your views here.
def home(request):
    d=Student.objects.all()
    return render(request,"home.html",{"d":d})
def add(request):
    if request.method =="POST":
        name=request.POST.get("name")
        rollno=request.POST.get("rollno")
        enroll=request.POST.get("enroll")
        batch=request.POST.get("batch")
        date=request.POST.get("date")
        Student.objects.create(name=name,rollno=rollno,enroll=enroll,batch=batch,date=date)
        return redirect("home")
    return render(request,"add.html")

def update(request,id):
    d=get_object_or_404(Student,id=id)
    if request.method =="POST":
        d.name=request.POST.get("name")
        d.rollno=request.POST.get("rollno")
        d.enroll=request.POST.get("enroll")
        d.batch=request.POST.get("batch")
        d.date=request.POST.get("date")
        d.save()
        return redirect("home")
    return render(request,"update.html",{"i":d})

def delete(request,id):
    d=get_object_or_404(Student,id=id)
    d.delete()
    return redirect("home")
