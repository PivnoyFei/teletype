from django.forms import ModelForm, Textarea

from .models import Post, Group, Comment, Message


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
        widgets = {"text": Textarea(attrs={"placeholder": "Напишите тут тваш пост"})}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        labels = {"text": "Текст комментария"}
        help_texts = {"text": "Напишите тут тваш комментарий"}
        widgets = {"text": Textarea(attrs={"placeholder": help_texts["text"]})}


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
            "slug": "Адрес для страницы в браузере должен быть коротким и английскими буквами",
            "description": "Дайте описание группе"
        }
