from django.forms import ModelForm, Textarea

from .models import Comment, Group, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("text", "group", "image")
        labels = {
            "text": "Текст",
            "group": "Группа",
            "image": "Изображение"
        }
        help_texts = {
            "text": "Текст нового поста",
            "group": "Группа, к которой будет относиться пост (Необязательно)",
            "image": "Добавить изображение к посту"
        }
        widgets = {
            "text": Textarea(attrs={"placeholder": "Напишите тут тваш пост"})
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        labels = {"text": "Текст комментария"}
        help_texts = "Напишите тут тваш комментарий"
        widgets = {"text": Textarea(attrs={"placeholder": help_texts})}


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ("title", "slug", "image", "avatar", "description")
        labels = {
            "title": "Название группы",
            "slug": "Адрес групп",
            "image": "Картинка",
            "avatar": "Аватар группы",
            "description": "Описание группы"
        }
        help_texts = {
            "title": "Дайте короткое название группе",
            "slug": "Адрес страницы в браузере, английскими буквами",
            "description": "Дайте описание группе"
        }
