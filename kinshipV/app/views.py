from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return render(req,'index.html')

def landpage(req):
    return render(req,'landing.html')

def formpage(req):
    return render(req,'form.html')