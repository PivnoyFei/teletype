from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000, verbose_name="Сообщение")

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return self.email
