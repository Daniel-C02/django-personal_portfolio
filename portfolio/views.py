from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()  #grabs all the objects from the db
    return render(request, 'portfolio/home.html', {'projects':projects})