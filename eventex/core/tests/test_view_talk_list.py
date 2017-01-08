from django.test import TestCase


class TalkListGet(TestCase):
    def test_get(self):
        response = self.client.get('/palestras/')
        self.assertEqual(200, response.status_code)
