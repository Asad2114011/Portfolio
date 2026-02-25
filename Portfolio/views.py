from django.shortcuts import render
from cp.models import cp
from project.models import project,Tag
from blog.models import blog

def home(request):
    cp_details=cp.objects.all()
    projects=project.objects.all()
    blogs=blog.objects.all()
    project_tag=Tag.objects.filter(projects__isnull=False).distinct()
    return render(request,'home.html',{'cp_details':cp_details,'projects':projects,'tag':project_tag,'blogs':blogs})