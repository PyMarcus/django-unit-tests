from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self) -> None:
        self.name = 'Elizabeth'
        self.email = 'elizabeth@email.com.br'
        self.subject = 'my beauty Elizabeth'
        self.message = 'hi,Elizabeth'

        self.data = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.data)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        request = self.client.post(reverse_lazy('index'), data={})
        self.assertNotEqual(request.status_code, 302)
