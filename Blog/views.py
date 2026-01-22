from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def Blogs(request):
    blogs=Blog.objects.all().order_by('-date')
    return render(request,'blogs.html',{'blogs':blogs})

def BlogDetail(request,pk):
    blog=get_object_or_404(Blog,pk=pk)
    return render(request,'blog_detail.html',{'blog':blog})