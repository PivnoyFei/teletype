from http import HTTPStatus as H

from django.core.cache import cache
from django.test import Client, TestCase
from django.urls import reverse

from posts.models import Group, Post, User


class PostURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username='HasNoName')
        cls.user_other = User.objects.create(username='OtherName')
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
        cls.URL_POST_CREATE = reverse('posts:post_create')
        cls.URL_LOGIN_NEXT = '/auth/login/?next=/create/'
        cls.URL_POST_DETAIL = reverse('posts:post_detail', args=(cls.post.pk,))
        cls.URL_POST_EDIT = reverse('posts:post_edit', args=(cls.post.pk,))
        cls.URL_FOLLOW = reverse('posts:follow_index')

        cls.url_status_code = {
            cls.URL_FOLLOW: [H.FOUND, 'posts/follow.html'],
            reverse('posts:index'): [H.OK, 'posts/index.html'],
            f'/group/{cls.post.group.slug}/': [H.OK, 'posts/group_list.html'],
            f'/profile/{cls.user.username}/': [H.OK, 'posts/profile.html'],
            cls.URL_POST_DETAIL: [H.OK, 'posts/post_detail.html'],
            cls.URL_POST_EDIT: [H.FOUND, 'posts/post_create.html'],
            cls.URL_POST_CREATE: [H.FOUND, 'posts/post_create.html'],
            reverse('users:signup'): [H.OK, 'users/signup.html'],
            reverse('users:login'): [H.OK, 'users/login.html'],
            '/unexisting_page/': [H.NOT_FOUND, 'core/404.html']
        }

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.authorized_client_other = Client()
        self.authorized_client_other.force_login(self.user_other)
        cache.clear()

    def test_guest_client_correct_tatus_code(self):
        """Проверяем доступность для гостей."""
        for url, code in self.url_status_code.items():
            with self.subTest(code=code):
                response = self.guest_client.get(url)
                self.assertEqual(response.status_code, code[0],
                                 f'''Страница {url} не найдена''')

    def test_post_create_exists_at_desired_location_authorized(self):
        """Страница доступна авторизованному пользователю."""
        url_status_code = {self.URL_FOLLOW: H.OK,
                           self.URL_POST_EDIT: H.OK,
                           self.URL_POST_CREATE: H.OK}
        for url, code in url_status_code.items():
            with self.subTest(code=code):
                response = self.authorized_client.get(url)
                self.assertEqual(response.status_code, code,
                                 f'''Страница {url} не найдена''')

    def test_post_create_redirect_anonymous_on_admin_login(self):
        """Перенаправление незарегестрированого пользователя."""
        response = self.guest_client.get(self.URL_POST_CREATE, follow=True)
        self.assertRedirects(response, self.URL_LOGIN_NEXT)
        """Перенаправление не автора поста со страницы редактирования."""
        response = self.authorized_client_other.get(
            self.URL_POST_EDIT, follow=True
        )
        self.assertRedirects(response, self.URL_POST_DETAIL)

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        for url, template in self.url_status_code.items():
            with self.subTest(template=template):
                response = self.authorized_client.get(url)
                self.assertTemplateUsed(
                    response, template[1],
                    f'''Страница {url} для шаблона {template} не найдена'''
                )

    def test_follow_redirect_anonymous_on_admin_login(self):
        """Перенаправление незарегестрированого пользователя."""
        response = self.guest_client.get(
            f'/profile/{self.user}/follow/', follow=True
        )
        self.assertRedirects(
            response, f'/auth/login/?next=/profile/{self.user}/follow/'
        )
        response = self.guest_client.get(
            f'/profile/{self.user}/unfollow/', follow=True
        )
        self.assertRedirects(
            response, f'/auth/login/?next=/profile/{self.user}/unfollow/'
        )
