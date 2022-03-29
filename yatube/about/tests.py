from http import HTTPStatus as H

from django.test import Client, TestCase
from django.urls import reverse


class StaticTests(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.url_status_code = {
            reverse('about:author'): [H.OK, 'about/author.html'],
            reverse('about:tech'): [H.OK, 'about/tech.html']
        }

    def test_about_url_exists_at_desired_location(self):
        """Страница доступна всем."""
        for adress, code in self.url_status_code.items():
            with self.subTest(adress=adress, code=code):
                response = self.guest_client.get(adress)
                self.assertEqual(response.status_code, code[0])

    def test_about_url_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        for address, template in self.url_status_code.items():
            with self.subTest(template=template):
                response = self.guest_client.get(address)
                self.assertTemplateUsed(response, template[1])
