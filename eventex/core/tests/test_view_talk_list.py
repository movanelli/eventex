from django.shortcuts import resolve_url as r
from django.test import TestCase


class TalkListGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, 'Título da Palestra'),
            (1, '10:00'),
            (1, '13:00'),
            (2, '/palestrantes/moises-meirelles'),
            (2, 'Moises Meirelles'),
            (2, 'Descrição da Palestra.'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)
