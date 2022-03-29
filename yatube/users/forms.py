from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

from .models import User, Profile

User = get_user_model()


class CreationForm(UserCreationForm):
    captcha = CaptchaField()
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            "bio", "location", "image", "avatar", "age",
            "birth_date", "job", "number"
        )
        labels = {
            "bio": "Биография", "location": "Город",
            "age": "Полных лет", "birth_date": "День рождения",
            "job": "Место работы", "number": "Номер телефона",
            "image": "Картинка", "avatar": "Изображение"
        }


class SocialForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            "github", "telegram", "vk"
        )
        labels = {
            "telegram": "аккаунт telegram",
            "github": "аккаунт github",
            "vk": "аккаунт vk"
        }
        help_texts = {
            "telegram": "https://t.me/",
            "github": "https://github.com/",
            "vk": "https://vk.com/"
        }
