from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post , Author 
from .forms import PostForm
# Create your views here.

class BlogHome(ListView):
    model = Post  
    context_object_name = 'posts' 
    template_name = 'django_blog/index.html'

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
     
    template_name = 'django_blog/post_create.html'

     
    def form_valid(self,PostForm):
        objects  = PostForm.save(commit=False)
        objects.author = self.request.user 
        objects.save()
        return super(PostCreate,self).form_valid(PostForm)
  
class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    slug_field = 'slug' 
    
    template_name = 'django_blog/post_detail.html'


class PostUpdate(UpdateView):
    model = Post 
    slug_field = 'slug'
    form_class = PostForm
    
    template_name = 'django_blog/post_update.html'

class PostDelete(DeleteView):
    model = Post 
    slug_field = 'slug'
    success_url = reverse_lazy('blog-home') 