# Create your views here.
import os
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.conf import settings
from extract.graphs import exctocsvtopandas, confmat
from toword.docxgen import doccreate

# def index(req):
#     return HttpResponse("Hello Peeps !! Corridoor") 

def index1(req):
    return render(req,'index.html')