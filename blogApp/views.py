from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost


class NewPost(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'body', 'image']
    template_name = 'blogApp/newPost.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class AllPost(ListView):
    model = BlogPost
    template_name = 'blogApp/index.html'
    context_object_name = 'post'
    ordering = ['-createdAt']


class DetailPost(DetailView):
    model = BlogPost
    template_name = 'blogApp/detailPost.html'
    context_object_name = 'post'


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'body', 'image']
    template_name = 'blogApp/newPost.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blogPost = self.get_object()
        if self.request.user == blogPost.author:
            return True
        return False


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    success_url = '/'
    template_name = 'blogApp/confirmDelete.html'

    def test_func(self):
        blogPost = self.get_object()
        if self.request.user == blogPost.author:
            return True
        return False
