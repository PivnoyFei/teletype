from django.contrib import admin

from .models import Group, Post, Comment
from users.models import Profile
from about.models import Contact


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "pk", "text", "pub_date", "author", "group", "image"
    )
    list_editable = ("group",)
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "author")
    search_fields = ("text", "author")
    empty_value_display = "-пусто-"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user", "bio", "age", "birth_date", "location", "avatar"
    )
    search_fields = ("user",)
    empty_value_display = "-пусто-"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group)
