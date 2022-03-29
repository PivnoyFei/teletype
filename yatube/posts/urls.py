from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('group/<slug:slug>/', views.group, name='group'),
    path('follow/', views.follow_index, name='follow_index'),
    path('group_index/', views.group_index, name='group_index'),
    path('group_create/', views.group_create, name='group_create'),
    path('group/<slug:slug>/edit/', views.group_edit, name='group_edit'),
    path('group/<slug:slug>/follow/', views.group_follow, name='group_follow'),
    path(
        'group/<slug:slug>/following/',
        views.group_following_list,
        name='group_following_list'
    ),
    path(
        'group/<slug:slug>/unfollow/',
        views.group_unfollow,
        name='group_unfollow'
    ),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('create/', views.post_create, name='post_create'),
    path(
        'posts/<int:post_id>/comment/',
        views.add_comment,
        name='add_comment'
    ),
    path(
        'posts/<int:post_id>/comment/<int:comment_id>/',
        views.comment_edit,
        name='comment_edit'
    ),
    path('posts/<int:post_id>/add_like/', views.add_like, name='add_like'),
    path(
        'posts/<int:post_id>/add_dislike/',
        views.add_dislike,
        name='add_dislike'
    ),
    path(
        'profile/<str:username>/following/',
        views.following_list,
        name='following_list'
    ),
    path(
        'profile/<str:username>/follower/',
        views.follower_list,
        name='follower_list'
    ),
    path(
        'profile/<str:username>/follow/',
        views.profile_follow, 
        name='profile_follow'
    ),
    path(
        'profile/<str:username>/unfollow/',
        views.profile_unfollow,
        name='profile_unfollow'
    ),
]
