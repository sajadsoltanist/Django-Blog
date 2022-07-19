from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView

from .models import Post, Comment
from .form import CommentForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostView(DetailView):
    model = Post
    template_name = "core/post.html"