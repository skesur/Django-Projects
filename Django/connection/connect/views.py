from django.shortcuts import render
import os
import requests
os.environ["no_proxy"] ="127.0.0.1,localhost"
# Create your views here.
def home(req):
    data = requests.get("http://127.0.0.1:8000/cricket/")
    data = data.json()
    return render(req,'home.html',{"d":data})