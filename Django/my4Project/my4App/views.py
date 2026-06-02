from django.shortcuts import render
from .models import CricketTeam
# Create your views here.
def home(request):
    name=request.GET.get("name")
    member=request.GET.get("member")
    date=request.GET.get("date")
    if name and member and date:
        CricketTeam.objects.create(name=name,member=member,date=date)
    return render(request,"home.html")

def show(request):
    se = request.GET.get("search")
    if se:
        data = CricketTeam.objects.filter(name__icontains=se)
    else:
        data = CricketTeam.objects.all()
    return render(request,"show.html",{"data":data})