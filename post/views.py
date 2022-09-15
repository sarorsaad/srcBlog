from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from.models import Post
from . import forms

# Create your views here.
class PostList(ListView):
    model = Post
    form_class = forms.PostForm

class PostDetail(DetailView):
     model = Post
     form_class = forms.PostForm
    
class PostDelete(DeleteView):
    model = Post
    form_class = forms.PostForm

class PostCreate(CreateView):
    model = Post
    form_class = forms.PostForm

class PostUpdate(UpdateView):
    model = Post
    form_class = forms.PostForm
    
