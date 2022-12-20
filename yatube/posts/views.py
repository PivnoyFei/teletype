from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, GroupForm, PostForm
from .models import (Comment, CustomUser, Dislike, Follow, FollowGroup, Group,
                     Like, Post)


def count_all(count):
    if count % 10 == 1 and count // 10 != 1:
        count = ["Публикация", "Подписчик", "Подписка"]
    elif 2 <= count % 10 <= 4 and count != 0 and count // 10 != 1:
        count = ["Публикации", "Подписчика", "Подписки"]
    else:
        count = ["Публикаций", "Подписчиков", "Подписок"]
    return count


def search(request):
    search_query = request.GET.get("search")
    if search_query and search_query != ' ':
        if search_query[0] == "@":
            user = CustomUser.objects.filter(username=search_query[1:])
            if not user:
                return redirect("posts:index")
            return redirect(
                "posts:profile", username=search_query[1:]
            )
        else:
            page_obj = Group.objects.filter(
                Q(title__icontains=search_query)
                | Q(slug__icontains=search_query)
            )[:10]
            context = {"page_obj": page_obj,
                       "search_query": search_query}
            return render(request, "posts/search.html", context)
    else:
        return render(request, "posts/search.html", {"page_obj": []})


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, settings.COUNT_POSTS)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "posts/index.html", context)


@login_required
def group_create(request):
    form = GroupForm(
        request.POST or None, files=request.FILES or None
    )
    if form.is_valid():
        group = form.save(commit=False)
        group.administrator = request.user
        group.save()
        return redirect("posts:profile", group.administrator)
    page_obj = Group.objects.filter(administrator=request.user)
    context = {"page_obj": page_obj, "form": form}
    return render(request, "posts/group/group_create.html", context)


@login_required
def group_edit(request, slug):
    group = get_object_or_404(Group, slug=slug)
    if request.user != group.administrator:
        return redirect("posts:profile", request.user)
    form = GroupForm(
        request.POST or None,
        files=request.FILES or None,
        instance=group
    )
    if form.is_valid():
        form.save()
        return redirect("posts:group_edit", slug=slug)
    page_obj = Group.objects.filter(administrator=request.user)
    context = {"is_edit": True,
               "page_obj": page_obj,
               "group": group,
               "form": form}
    return render(request, "posts/group/group_create.html", context)


def group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    post_all = count_all(post_list.count())
    follow_all = count_all(group.group_following.all().count())
    paginator = Paginator(post_list, settings.COUNT_POSTS)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    following = FollowGroup.objects.filter(
        user=request.user, group=group
    )
    context = {"group": group,
               "follow_all": follow_all[1],
               "following": following,
               "post_all": post_all[0],
               "page_obj": page_obj}
    return render(request, "posts/group/group_list.html", context)


def profile(request, username):
    author = get_object_or_404(CustomUser, username=username)
    author_list = author.posts.all()
    post_all = count_all(author_list.count())
    paginator = Paginator(author_list, settings.COUNT_POSTS)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    following_all = count_all(author.following.all().count())
    follower_all = count_all(author.follower.all().count())
    following = Follow.objects.filter(
        user__username=request.user, author=author
    )
    context = {"author": author,
               "post_all": post_all[0],
               "page_obj": page_obj,
               "following": following,
               "follower_all": follower_all[2],
               "following_all": following_all[1]}
    return render(request, "posts/profile.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)
    comments = post.comments.all()
    author = post.author
    user = request.user
    if request.user.username:
        like = Like.objects.filter(post_id=post_id, users=user)
        dislike = Dislike.objects.filter(post_id=post_id, users=user)
        following = Follow.objects.filter(
            user__username=user, author=author
        )
    else:
        like = None
        dislike = None
        following = None
    context = {"post": post,
               "form": form,
               "like": like,
               "dislike": dislike,
               "author": author,
               "following": following,
               "comments": comments}
    return render(request, "posts/post_detail.html", context)


@login_required
def post_create(request):
    form = PostForm(
        request.POST or None, files=request.FILES or None
    )
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("posts:profile", post.author)
    return render(request, "posts/post_create.html", {"form": form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        return redirect("posts:post_detail", post_id=post_id)
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post
    )
    if form.is_valid():
        post.edit = True
        form.save()
        return redirect("posts:post_detail", post_id=post_id)
    context = {"is_edit": True,
               "post": post,
               "form": form}
    return render(request, "posts/post_create.html", context)


@login_required
def add_like(request, post_id):
    try:
        dislike = Dislike.objects.get(post_id=post_id, users=request.user)
        if dislike.users == request.user:
            dislike.delete()
            Like.objects.create(users=request.user, post_id=post_id)
    except Dislike.DoesNotExist:
        try:
            like = Like.objects.get(post_id=post_id, users=request.user)
            if like.users == request.user:
                like.delete()
        except Like.DoesNotExist:
            Like.objects.create(users=request.user, post_id=post_id)
    return redirect("posts:post_detail", post_id=post_id)


@login_required
def add_dislike(request, post_id):
    try:
        like = Like.objects.get(post_id=post_id, users=request.user)
        if like.users == request.user:
            like.delete()
            Dislike.objects.create(users=request.user, post_id=post_id)
    except Like.DoesNotExist:
        try:
            dislike = Dislike.objects.get(
                post_id=post_id, users=request.user
            )
            if dislike.users == request.user:
                dislike.delete()
        except Dislike.DoesNotExist:
            Dislike.objects.create(users=request.user, post_id=post_id)
    return redirect("posts:post_detail", post_id=post_id)


@login_required
def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        return redirect("posts:post_detail", post_id)


@login_required
def comment_edit(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        return redirect("posts:post_detail", post_id=post_id)
    form = CommentForm(
        request.POST or None,
        files=request.FILES or None,
        instance=comment
    )
    if form.is_valid():
        comment.edit = True
        form.save()
        return redirect("posts:post_detail", post_id=post_id)
    context = {"is_edit": True,
               "post": post,
               "form": form}
    return render(request, "posts/post_detail.html", context)


@login_required
def following_list(request, username):
    author = get_object_or_404(CustomUser, username=username)
    page_obj = author.following.all()
    context = {"is_edit": True, "page_obj": page_obj, "author": author}
    return render(request, "posts/follow/following_list.html", context)


@login_required
def follower_list(request, username):
    author = get_object_or_404(CustomUser, username=username)
    page_obj = author.follower.all()
    context = {"page_obj": page_obj, "author": author}
    return render(request, "posts/follow/follower_list.html", context)


@login_required
def follow_index(request):
    post_list = Post.objects.filter(
        author__following__user=request.user
    )
    paginator = Paginator(post_list, settings.COUNT_POSTS)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "posts/follow/follow.html", context)


@login_required
def profile_follow(request, username):
    author = get_object_or_404(CustomUser, username=username)
    if author != request.user:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect("posts:profile", username)


@login_required
def profile_unfollow(request, username):
    get_object_or_404(Follow, user=request.user,
                      author__username=username).delete()
    return redirect("posts:profile", username)


@login_required
def group_index(request):
    post_list = Post.objects.filter(
        group__group_following__user=request.user
    )
    paginator = Paginator(post_list, settings.COUNT_POSTS)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "posts/group/group_follow.html", context)


@login_required
def group_following_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    page_obj = group.group_following.all()
    context = {"page_obj": page_obj, "group": group}
    return render(request, "posts/follow/following_list.html", context)


@login_required
def group_follow(request, slug):
    group = get_object_or_404(Group, slug=slug)
    FollowGroup.objects.get_or_create(user=request.user, group=group)
    return redirect("posts:group", slug)


@login_required
def group_unfollow(request, slug):
    group = get_object_or_404(Group, slug=slug)
    get_object_or_404(FollowGroup, user=request.user,
                      group=group).delete()
    return redirect("posts:group", slug)
