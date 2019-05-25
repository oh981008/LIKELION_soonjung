from django.shortcuts import render
from .models import Mysite

def home(request):
    mysites=Mysite.objects
    return render(request,'home.html',{'mysites':mysites})

# Create your views here.
