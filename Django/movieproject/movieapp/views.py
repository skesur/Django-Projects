from django.shortcuts import render
from .models import movies

# Create your views here.
def home(request):
    movie=movies.objects.all()
    return render(request,"home.html",{"movie":movie})