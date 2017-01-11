from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Talk


class TalkListGet(TestCase):
    def setUp(self):
        Talk.objects.create(title='Título da Palestra', start='10:00',
                            description='Descrição da Palestra.')
        Talk.objects.create(title='Título da Palestra', start='13:00',
                            description='Descrição da Palestra.')

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

    def test_context(self):
        variables = ['morning_talks', 'afternoon_talks']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)
