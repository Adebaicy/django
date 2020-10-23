from django.shortcuts import render
from portf.models import Project

def home(request):
    projects=Project.objects.all()#grabs element from that database
    return render(request, "portfolio.html", {'projects':projects})

