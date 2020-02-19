from django.forms import ModelForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from webapp.models import Post, Comment, PostsComments


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


def book_list(request, template_name='posts_list.html'):
    posts = Post.objects.all()
    data = {}
    data['post_list'] = posts
    data['form'] = PostForm
    return render(request, template_name, data)


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', context={
        'post': post,
        'comments': post.postscomments_set.all()
    })


def post_create(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = Post.objects.create(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                author=request.user
            )
            return redirect('post_detail', post.pk)
        else:
            return render(request, 'create.html', context={'form': form})


def post_update_view(request, pk, template_name='partial/form.html'):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', post.pk)
    return render(request, template_name, {'form': form})


def post_delete(request, pk, template_name='post_delete.html'):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, template_name, {'post': post})


class CommentCreateView(View):
    def post(self, request):
        # post_id = request.POST.get('post_id')
        # text = request.POST.get('text')
        print(request.POST)
        # obj = Comment.objects.create(user=self.request.user, text=text)
        # print(obj)
        return JsonResponse({'status': 'ok'})
