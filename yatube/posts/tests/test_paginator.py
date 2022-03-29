from django.test import Client, TestCase
from django.urls import reverse

from posts.models import Group, Post, User


class PaginatorViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username='HasNoName')
        cls.group = Group.objects.create(
            title='Тестовое название группы',
            slug='test-slug',
            description='Тестовое описание'
        )
        cls.post = [Post.objects.create(
            author=cls.user,
            group=cls.group,
            text='Тестовый текст' + str(i)) for i in range(13)]
        cls.user_other = User.objects.create(username='OtherName')
        cls.group_other = Group.objects.create(
            title='Тестовое название',
            slug='tests-slugs',
            description='Тестовое описание группы'
        )
        cls.post_other = Post.objects.create(
            author=cls.user_other,
            group=cls.group_other,
            text='Тестовый текст'
        )
        cls.guest_client = Client()
        cls.URL_INDEX = reverse('posts:index')
        cls.URL_GROUP = reverse('posts:group_list', args=(cls.group.slug,))
        cls.URL_OTHER_GROUP = reverse(
            'posts:group_list', args=(cls.group_other.slug,)
        )
        cls.URL_PROFILE = reverse('posts:profile', args=(cls.user,))
        cls.URL_OTHER_PROFILE = reverse(
            'posts:profile', args=(cls.user_other,)
        )

    def test_paginator_index_group_profile(self):
        """13 тестовых записей для пагинатора."""
        url_code = {
            self.URL_INDEX, self.URL_GROUP, self.URL_PROFILE,
            self.URL_OTHER_GROUP, self.URL_OTHER_PROFILE
        }
        for url in url_code:
            response = self.guest_client.get(url)
            if url in (self.URL_OTHER_GROUP, self.URL_OTHER_PROFILE):
                self.assertEqual(len(response.context['page_obj']), 1)
            else:
                self.assertEqual(len(response.context['page_obj']), 10)
                response = self.guest_client.get(url + '?page=2')
                if url == self.URL_INDEX:
                    self.assertEqual(len(response.context['page_obj']), 4, )
                else:
                    self.assertEqual(len(response.context['page_obj']), 3, )
