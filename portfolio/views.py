from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import Project

def home(request):
    records=Project.objects.all()
    return render(request,'portfolio/home.html',{'records':records})

