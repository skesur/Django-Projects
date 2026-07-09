from django.shortcuts import render
import os
import requests
from openpyxl import Workbook
from django.http import HttpResponse
os.environ["no_proxy"] ="127.0.0.1,localhost"
# Create your views here.
def home(req):
    data = requests.get("http://127.0.0.1:8000/cricket/")
    data = data.json()

    return render(req,'home.html',{"d":data})

def download(req):
    data = requests.get("http://127.0.0.1:8000/cricket/")
    data = data.json()

    wb = Workbook()
    ws = wb.active
    ws.title = "CRICKET PLAYERS"
    ws.append(["Team name","Runs","Captain name","Date"])
    for i in data:
        ws.append([i.get("team"),i.get("run"),i.get("cap"),i.get("date")])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="cricket.xlsx"'
    wb.save(response)

    return response

