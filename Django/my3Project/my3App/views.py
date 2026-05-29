from django.shortcuts import render
data = {
    "name":"Saumya",
    "age":20,
    "marks":[20,20,25,25,23],
    "n":["aaaa","bbb","cc","ddddd","e"]
}
# Create your views here.
def fun1(request):
    return render(request,"1.html",{"d":data})
def fun2(request):
    return render(request,"2.html",{"d":data})