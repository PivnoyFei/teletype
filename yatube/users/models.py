from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Автор"
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        verbose_name = "Полных лет"
    )
    birth_date = models.DateField(
        blank=True, null=True, verbose_name = "Дата рождения"
    )
    bio = models.TextField(
        blank=True,
        null=True,
        max_length=300, 
        verbose_name = "Обо мне",
        help_text="Раскажите о себе"
    )
    location = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name = "Город",
    )
    image = models.ImageField(
        verbose_name="Картинка",
        upload_to="avatar/",
        blank=True,
        null=True,
        help_text="Загрузите картинку"
    )
    avatar = models.ImageField(
        verbose_name="Аватарка",
        blank=True,
        null=True, 
        upload_to="avatar/",
        help_text="Загрузите аватарку"
    )
    job = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name = "Место работы"
    )
    number =  models.CharField(
        blank=True,
        null=True,
        max_length=15,
        verbose_name = "Телефон"
    )
    github = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    vk = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)