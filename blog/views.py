from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def home(request):
   return  render (request,"blog/home.html",context={"posts":Post.objects.all()})

def about(request):
   return render(request,"blog/about.html")

   

