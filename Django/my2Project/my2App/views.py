from django.shortcuts import render
data = {"name":"Saumya","des":"FSD","age":20}
# Create your views here.
def home(request):
    return render(request,"1.html",{"dataD":data})
def about(request):
    return render(request,"2.html")
def contact(request):
    return render(request,"3.html")
def n(request):
    return render(request,"n.html",{"dataD":data})
def a(request):
    return render(request,"a.html",{"dataD":data})
def d(request):
    return render(request,"d.html",{"dataD":data})