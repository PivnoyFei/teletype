from django.test import TestCase

from posts.models import Comment, Follow, Group, Post, User


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_follow = User.objects.create(username='FollowUser')
        cls.user = User.objects.create(username='HasNoName')
        cls.group = Group.objects.create(
            title='Тестовое название группы',
            slug='test-slug',
            description='Тестовое описание'
        )
        cls.post = Post.objects.create(
            author=cls.user,
            group=cls.group,
            text='Тестовый текст',
        )
        cls.comment = Comment.objects.create(
            author=cls.user,
            post=cls.post,
            text='Тестовый комментарий'
        )
        cls.follow = Follow.objects.create(
            user=cls.user_follow,
            author=cls.user
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        post = PostModelTest.post
        group = PostModelTest.group
        comment = PostModelTest.comment
        self.assertEqual(post.text[:15], str(post))
        self.assertEqual(group.title, str(group))
        self.assertEqual(comment.text, str(comment))

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        post = PostModelTest.post
        field_verboses = {
            'text': 'Текст поста',
            'pub_date': 'Дата публикации',
            'author': 'Автор',
            'group': 'Группы',
            'image': 'Картинка'
        }
        for field, expected in field_verboses.items():
            with self.subTest(field=field):
                response = post._meta.get_field(field).verbose_name
                self.assertEqual(response, expected)

    def test_group_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        group = PostModelTest.group
        field_verboses = {
            'title': 'Заголовок',
            'slug': 'Адрес группы',
            'description': 'Описание группы',
        }
        for field, expected in field_verboses.items():
            with self.subTest(field=field):
                response = group._meta.get_field(field).verbose_name
                self.assertEqual(response, expected)

    def test_comment_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        comment = PostModelTest.comment
        field_verboses = {
            'post': 'Комментарий',
            'author': 'Автор',
            'text': 'Текст коментария',
            'created': 'Дата комментария',
        }
        for field, expected in field_verboses.items():
            with self.subTest(field=field):
                response = comment._meta.get_field(field).verbose_name
                self.assertEqual(response, expected)

    def test_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        post = PostModelTest.post
        field_help_texts = {
            'text': 'Введите текст поста',
            'group': 'Группа, к которой будет относиться пост',
            'image': 'Загрузите картинку'
        }
        for field, expected in field_help_texts.items():
            with self.subTest(field=field):
                response = post._meta.get_field(field).help_text
                self.assertEqual(response, expected)

    def test_group_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        group = PostModelTest.group
        field_help_texts = {
            'title': 'Дайте короткое название группе',
            'slug': 'Адрес для странице в браузере',
            'description': 'Дайте описание группе',
        }
        for field, expected in field_help_texts.items():
            with self.subTest(field=field):
                response = group._meta.get_field(field).help_text
                self.assertEqual(response, expected)

    def test_comment_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        comment = PostModelTest.comment
        field_verboses = {
            'post': 'Комментарий поста',
            'author': 'Автор комментария',
            'text': 'Введите текст коментария',
            'created': 'Дата создания комментария',
        }
        for field, expected in field_verboses.items():
            with self.subTest(field=field):
                response = comment._meta.get_field(field).help_text
                self.assertEqual(response, expected)

    def test_follow_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        follow = PostModelTest.follow
        field_verboses = {
            'user': 'Подписчик',
            'author': 'Автор',
        }
        for field, expected in field_verboses.items():
            with self.subTest(field=field):
                response = follow._meta.get_field(field).verbose_name
                self.assertEqual(response, expected)
