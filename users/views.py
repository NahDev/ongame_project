from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return render(request, "post_list.html")
    else:
        form = PostForm()
    return render(request, "create_post.html", {"form": form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})
