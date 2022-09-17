from django.shortcuts import render
from django.urls import reverse_lazy
from recipe_crud.models import Post
from recipe_crud.forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                DetailView, CreateView,
                                UpdateView, DeleteView)
# Create your views here.

class  CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'recipe_crud/recipe_form.html'
    model = Post
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin,UpdateView):
#     login_url = '/login/'
    template_name = 'recipe_crud/recipe_form.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('recipe_crud:list')
    context_object_name = 'recipes'
    template_name = 'recipe_crud/recipe_confirm_delete.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class PostListView(ListView):
    context_object_name = 'recipes'
    template_name = 'recipe_crud/recipe_list.html'
    model = Post
    ordering = ['recipe_name']
    # paginate_by = 2


class PostDetailView(DetailView):
    context_object_name = 'recipes_detail'
    model = Post
    template_name = 'recipe_crud/recipe_detail.html'


