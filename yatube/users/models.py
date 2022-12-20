from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    GENDERS = (
        ("m", "Мужчина"),
        ("f", "Женщина"),
    )

    gender = models.CharField("Пол", max_length=1, choices=GENDERS, default="")
    age = models.IntegerField("Полных лет", blank=True, null=True)
    birth_date = models.DateField("Дата рождения", null=True)
    bio = models.TextField("Обо мне", blank=True, null=True, max_length=300)
    location = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Город",
    )
    avatar = models.ImageField(
        verbose_name="Аватарка",
        blank=True,
        null=True,
        upload_to="avatar/",
        help_text="Загрузите аватарку",
    )
    job = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Место работы",
    )
    number = models.CharField(
        blank=True,
        null=True,
        max_length=15,
        verbose_name="Телефон",
    )
    github = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    vk = models.CharField(max_length=100, null=True, blank=True)
