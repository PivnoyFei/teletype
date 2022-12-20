from http import HTTPStatus as H

from django.core.cache import cache
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse
from posts.forms import PostForm
from posts.models import Comment, Follow, Group, Post, User


class PostViewsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_follow = User.objects.create(username='FollowUser')
        cls.user = User.objects.create(username='HasNoName')
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00'
            b'\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00'
            b'\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        cls.image = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )
        cls.group = Group.objects.create(
            title='Тестовое название группы',
            slug='test-slug',
            description='Тестовое описание'
        )
        cls.post = Post.objects.create(
            author=cls.user,
            group=cls.group,
            image=cls.image,
            text='Тестовый текст',
        )

        cls.user_other = User.objects.create(username='OtherName')
        cls.group_other = Group.objects.create(
            title='Тестовое название группы',
            slug='test-other-slug',
            description='Тестовое описание 2'
        )

        cls.URL_INDEX = reverse('posts:index')
        cls.URL_POST_CREATE = reverse('posts:post_create')
        cls.URL_GROUP = reverse('posts:group_list', args=(cls.group.slug,))
        cls.URL_PROFILE = reverse('posts:profile', args=(cls.user,))
        cls.URL_POST_DETAIL = reverse('posts:post_detail', args=(cls.post.pk,))
        cls.URL_POST_EDIT = reverse('posts:post_edit', args=(cls.post.pk,))

        cls.templates_page_names = {
            cls.URL_GROUP: 'posts/group_list.html',
            cls.URL_PROFILE: 'posts/profile.html',
            cls.URL_POST_DETAIL: 'posts/post_detail.html',
            cls.URL_POST_EDIT: 'posts/post_create.html',
            cls.URL_POST_CREATE: 'posts/post_create.html',
            reverse('users:signup'): 'users/signup.html',
            '/auth/login/?next=/create/': 'users/login.html'
        }

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.authorized_client_other = Client()
        self.authorized_client_other.force_login(self.user_other)

    def test_pages_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        for url, template in self.templates_page_names.items():
            with self.subTest(template=template):
                response = self.authorized_client.get(url)
                self.assertTemplateUsed(
                    response, template,
                    f'''Страница {url} для шаблона {template} не найдена'''
                )

    def test_page_show_correct_context(self):
        """Шаблон с правильным контекстом."""
        url_code = {self.URL_INDEX, self.URL_GROUP,
                    self.URL_PROFILE, self.URL_POST_DETAIL}
        for url in url_code:
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                if url == self.URL_POST_DETAIL:
                    first_object = response.context.get('post')
                else:
                    self.assertEqual(len(response.context['page_obj']), 1)
                    first_object = response.context.get('page_obj')[0]
                self.assertEqual(first_object.pk, self.post.pk)
                self.assertEqual(first_object.text, self.post.text)
                self.assertEqual(first_object.image, self.post.image)
                self.assertEqual(first_object.author, self.post.author)
                self.assertEqual(first_object.group.slug, self.group.slug)
                self.assertEqual(first_object.group.title, self.group.title)
                self.assertEqual(first_object.group.description,
                                 self.group.description)

    def test_posts_page_show_correct_context(self):
        """Шаблон сформирован с правильным контекстом."""
        urls = {self.URL_POST_CREATE, self.URL_POST_EDIT}
        for url in urls:
            response = self.authorized_client.get(url)
            form_fields = {'text', 'group', 'image', 'is_edit'}
            for value in form_fields:
                with self.subTest(value=value):
                    form_field = response.context.get('form')
                    self.assertIsInstance(form_field, PostForm)

    def test_comment_add_post(self):
        """Проверка добавления коммента к посту."""
        Comment.objects.count()
        comment = {
            'author': self.user,
            'text': 'Тестовый коммент'
        }
        response = self.authorized_client.post(
            reverse('posts:add_comment', args=(self.post.id,)),
            data=comment,
            follow=True
        )
        self.assertRedirects(response, reverse(
            'posts:post_detail',
            args=(self.post.id,)))
        self.assertEqual(Comment.objects.count(), 1)
        self.assertTrue(Comment.objects.filter(
            text='Тестовый коммент',
            author=self.user).exists())
        self.assertEqual(response.status_code, H.OK)

    def test_follow_user(self):
        """Посты подписчиков в ленте follow_index."""
        self.authorized_client.get(reverse(
            'posts:profile_follow',
            args=(self.user_other.username,)))
        post_other = Post.objects.create(
            author=self.user_other,
            group=self.group_other,
            image=self.image,
            text='Тестовый текст 2',
        )
        response = self.authorized_client.get(reverse(
            'posts:follow_index'))
        self.assertEqual(len(response.context['page_obj']), 1)
        first_object = response.context.get('page_obj')[0]
        self.assertEqual(first_object.pk, post_other.pk)
        self.assertEqual(first_object.text, post_other.text)
        self.assertEqual(first_object.image, post_other.image)
        self.assertEqual(first_object.author, post_other.author)
        self.assertEqual(first_object.group.slug, self.group_other.slug)
        self.assertEqual(first_object.group.title, self.group_other.title)
        self.assertEqual(first_object.group.description,
                         self.group_other.description)

    def test_following_user(self):
        """Подписка и отписка на автора."""
        Follow.objects.count()
        response = self.authorized_client.get(reverse(
            'posts:profile_follow', args=(self.user_follow,)))
        self.assertRedirects(response, reverse(
            'posts:profile', args=(self.user_follow,)))
        self.assertEqual(Follow.objects.count(), 1,
                         "Проверьте, что правильно считаются подписки")

        self.assertTrue(
            Follow.objects.filter(
                user=self.user, author=self.user_follow
            ).exists()
        )
        response = self.authorized_client.get(reverse(
            'posts:profile_unfollow', args=(self.user_follow,)))
        self.assertRedirects(response, reverse(
            'posts:profile', args=(self.user_follow,)))
        self.assertEqual(Follow.objects.count(), 0,
                         "Проверьте, что правильно считаются оnписки")

    def test_cache_index(self):
        """Проверка кеширования."""
        post_test = Post.objects.create(
            author=self.user,
            text='Проверка кеша',
        )
        post_add = self.authorized_client.get(self.URL_INDEX).content
        post_test.delete()
        post_deleted = self.authorized_client.get(self.URL_INDEX).content
        self.assertEqual(post_add, post_deleted)
        cache.clear()
        cache_cleared = self.authorized_client.get(self.URL_INDEX).content
        self.assertNotEqual(post_add, cache_cleared)
