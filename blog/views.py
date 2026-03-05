from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

def home(request):
   return  render (request,"blog/home.html",context={"posts":Post.objects.all()})

class PostListView(ListView):
   model=Post
   template_name="blog/home.html"
   ordering=["-time"]
   context_object_name="posts"

class PostDetailView(DetailView):
   model=Post
   ordering=["-time"]

class PostCreateView(LoginRequiredMixin,CreateView):
   model=Post
   fields=["title","content"] 
   
   def form_valid(self, form):
       form.instance.author=self.request.user
       return super().form_valid(form)
   
class PostUpdateView(LoginRequiredMixin,UpdateView,UserPassesTestMixin):
   model=Post
   fields=["title","content"] 
   
   def form_valid(self, form):
       form.instance.author=self.request.user
       return super().form_valid(form)
   
   def test_func(self):
      post=self.get_object()
      if self.request.user == post.author:
         return True
      return False
   
def about(request):
   return render(request,"blog/about.html")

class PostDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
   model=Post
   success_url='/'
   
   def test_func(self):
      post=self.get_object()
      if self.request.user == post.author:
         return True
      return False
   

   

