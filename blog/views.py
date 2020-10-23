

from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def blog(request):
    blog=Blog.objects.all()#grabs element from that database
    return render(request, "blog/blog.html", {'blogs':blog})
def story(request, iid):
    blogi=get_object_or_404(Blog, pk=iid)
    return render(request,"blog/fuck.html", {'iiid':blogi})