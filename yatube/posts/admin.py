from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Group, Post, Comment
from users.models import CustomUser
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


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "gender",
                    "birth_date",
                    "groups",
                )
            }
        )
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group)
