from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

CustomUser = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        db_index=True,
        help_text="Дайте короткое название группе",
        verbose_name="Заголовок"
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        help_text="Адрес для странице в браузере",
        verbose_name="Адрес группы"
    )
    description = models.TextField(
        blank=True, null=True,
        help_text="Дайте описание группе",
        verbose_name="Описание группы"
    )
    image = models.ImageField(
        verbose_name="Картинка",
        upload_to="group/",
        blank=True,
        null=True,
        help_text="Загрузите картинку"
    )
    avatar = models.ImageField(
        verbose_name="Аватарка",
        blank=True,
        null=True,
        upload_to="group/",
        help_text="Загрузите аватарку"
    )
    administrator = models.ForeignKey(
        CustomUser, blank=True, null=True,
        on_delete=models.CASCADE,
        related_name="group_admin",
        verbose_name='Администратор'
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        "Текст", help_text="Введите текст поста"
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Дата публикации"
    )
    Time_updated = models.DateTimeField(
        "Дата обновления", auto_now=True
    )
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор"
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name="Группы",
        help_text="Группа, к которой будет относиться пост"
    )
    image = models.ImageField(
        verbose_name="Картинка",
        upload_to="posts/",
        blank=True,
        null=True,
        help_text="Загрузите картинку"
    )
    edit = models.BooleanField(
        default=False, verbose_name="Отредактирован"
    )
    tags = models.ForeignKey(
        "Tag",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Тег"
    )

    class Meta:
        ordering = ("-Time_updated", "-pub_date",)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.text[:15]

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="comments",
        verbose_name="Комментарий",
        help_text="Комментарий поста"
    )
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор"
    )
    text = models.TextField(
        verbose_name="Текст коментария",
        help_text="Введите текст коментария"
    )
    created = models.DateTimeField(
        verbose_name="Дата комментария",
        auto_now_add=True
    )
    edit = models.BooleanField(
        default=False, verbose_name="Отредактирован"
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="like"
    )
    users = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_like"
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('post', 'users',),
                name='unique_like'
            ),
        )


class Dislike(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="dislike"
    )
    users = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_dislike"
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('post', 'users',),
                name='unique_dislike'
            ),
        )


class Follow(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name='Автор'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author',),
                name='unique_follow'
            ),
        )


class FollowGroup(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="group_follower",
        verbose_name='Подписчик'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="group_following",
        verbose_name='Группа'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'group',),
                name='unique_follow'
            ),
        )


class Message(models.Model):
    from_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="from_user"
    )
    to_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="to_user"
    )
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created",)
