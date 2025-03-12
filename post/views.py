from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Media, Like, Comment
from .form import PostForm, MediaForm, CommentForm


@login_required
def create_post(request):
    """
    Create a new post with optional media upload.
    """
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        media_form = MediaForm(request.POST, request.FILES)
        if post_form.is_valid() and media_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            # Save media if uploaded
            media = media_form.save(commit=False)
            media.post = post
            media.save()
            return redirect('/')  # Redirect to the home or post detail
    else:
        post_form = PostForm()
        media_form = MediaForm()

    return render(request, 'posts/post_create.html', {
        'post_form': post_form,
        'media_form': media_form,
    })


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        if request.user in post.likes.all():
            post.likes.remove(request.user)  # Unlike
            liked = False
        else:
            post.likes.add(request.user)  # Like
            liked = True

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Handle AJAX requests
            return JsonResponse({'liked': liked, 'like_count': post.likes.count()})

        # Redirect back to the post detail page
        return redirect('post_detail', pk=post.id)


@login_required
def comment_post(request, post_id):
    """
    Add a comment to a post.
    """
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)  # Redirect to post detail
    else:
        form = CommentForm()

    return render(request, 'posts/post_detail.html', {'form': form, 'post': post})


def post_detail(request, pk):
    # Hole den Post anhand der ID (pk)
    post = get_object_or_404(Post, id=pk)

    # Bereite den Kontext für das Template vor
    context = {
        'post': post,
    }

    # Rendere die Detailseite mit den Postdaten
    return render(request, 'posts/post_detail.html', context)