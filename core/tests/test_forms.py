from django.test import TestCase
from model_mommy import mommy
from core.forms import ContactForm


class ContactFormTestCase(TestCase):
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

        self.form = ContactForm(data=self.data)

    def test_send_mail(self) -> None:
        form1 = ContactForm(data=self.data)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)
