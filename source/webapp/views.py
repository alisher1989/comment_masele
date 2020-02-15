from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.contrib import auth
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import PostCommentForm, CommentForm
from webapp.models import Post, PostsComments, Comment


class PostsListView(ListView):
    model = Post
    template_name = 'posts_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_post(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['post_comments'] = self.get_post().postscomments_set.all()
        return context


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = PostCommentForm

    def create(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        a = PostsComments.objects.create(post_id_id=post.pk, comment_id=Comment.objects.last())
        return a

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        Comment.objects.create(
            user=self.request.user,
            **form.cleaned_data
        )
        self.create()
        return redirect('post_detail', pk=post.pk )


class CommentAddView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('posts_list')
