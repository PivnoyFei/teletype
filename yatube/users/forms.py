from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "first_name", "last_name", "username", "email", "gender",
            "birth_date"
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username", "first_name", "last_name", "email", "gender",
            "birth_date"
        )


class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name", "last_name", "bio", "location",
            "avatar", "age", "birth_date", "job", "number"
        )
        labels = {
            "bio": "Биография", "location": "Город",
            "age": "Полных лет", "birth_date": "День рождения",
            "job": "Место работы", "number": "Номер телефона",
            "avatar": "Изображение"
        }


class SocialForm(ModelForm):
    class Meta:
        model = CustomUser
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
