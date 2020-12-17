from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog

class BlogListView(ListView):
    template_name = 'blog-list.html'
    model = Blog

class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = Blog

class BlogCreateView(CreateView):
    template_name = 'blog-create.html'
    model = Blog
    fields = ['name', 'purchaser', 'description']

class BlogUpdateView(UpdateView):
    template_name = 'blog-update.html'
    model = Blog

class BlogDeleteView(DeleteView):
    template_name = 'blog-delete.html'
    model = Blog

