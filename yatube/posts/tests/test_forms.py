import shutil
import tempfile
from http import HTTPStatus as H

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from posts.forms import PostForm
from posts.models import Group, Post, User

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class PostCreateFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
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
        cls.form = PostForm()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_create_form(self):
        """Валидная форма создает запись в пост."""
        posts_count = Post.objects.count()
        form_data = {
            'text': self.post.text,
            'group': self.group.pk,
            'image': self.post.image,
        }
        response = self.authorized_client.post(
            reverse('posts:post_create'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(
            response, reverse('posts:profile', args=(self.user,))
        )
        self.assertEqual(Post.objects.count(), posts_count + 1)
        self.assertTrue(Post.objects.filter(
            text=form_data['text'],
            group=self.group.pk,
            image='posts/small.gif').exists())
        self.assertEqual(response.status_code, H.OK)

    def test_cant_create_existing_slug(self):
        """Редоктирование поста."""
        posts_count = Post.objects.count()
        form_data = {
            'text': 'Отредактированный текст',
            'group': self.group.pk
        }
        response = self.authorized_client.post(
            reverse('posts:post_edit', args=(self.post.id,)),
            data=form_data
        )
        self.assertRedirects(
            response,
            reverse('posts:post_detail', args=(self.post.id,))
        )
        self.assertEqual(Post.objects.count(), posts_count)
        self.assertTrue(Post.objects.filter(
            text=form_data['text'],
            group=self.group.pk).exists())
        self.assertEqual(response.status_code, H.FOUND)

    def test_text_label_and_help_text(self):
        title_label = PostCreateFormTests.form.fields['text'].label
        self.assertEqual(title_label, 'Текст')
        title_help_text = PostCreateFormTests.form.fields['text'].help_text
        self.assertEqual(title_help_text, 'Текст нового поста')

    def test_group_label_and_help_text(self):
        title_label = PostCreateFormTests.form.fields['group'].label
        self.assertEqual(title_label, 'Группа')
        title_help_text = PostCreateFormTests.form.fields['group'].help_text
        self.assertEqual(
            title_help_text,
            'Группа, к которой будет относиться пост (Необязательно)'
        )
