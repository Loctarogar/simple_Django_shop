from django.shortcuts import render, get_object_or_404
from .models import Post, Tag, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    tags = Tag.objects.all()
    posts = Post.objects.filter(status="published")

    paginator = Paginator(posts, 6)
    page = request.GET.get("page")
    blog_list = paginator.get_page(page)

    return render(request,
                  "blog/post_list.html",
                  {"posts": posts, "tags": tags,
                   "blog_list": blog_list})


def post_list_by_tag(request, tag_id=None):
    tags = Tag.objects.all()
    if tag_id:
        posts = Post.objects.filter(status="published",
                                    tag=tag_id)
    else:
        posts = Post.objects.filter(status="published")

    paginator = Paginator(posts, 6)
    page = request.GET.get("page")
    blog_list = paginator.get_page(page)

    return render(request, "blog/post_list.html",
                  {"posts": posts, "tags": tags,
                   "blog_list": blog_list})


def post_detail(request, year, month, day, post):
    tags = Tag.objects.all()
    post = get_object_or_404(Post,
                             status="published",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=post)
    comments = post.comments.filter(active=True)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.comment_author = request.user
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, "blog/post_detail.html",
                  {"post": post, "tags": tags,
                   "comments": comments,
                   "comment_form": comment_form})
