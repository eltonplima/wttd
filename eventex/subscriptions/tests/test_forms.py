from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeFormTest(TestCase):
    def test_has_fields(self):
        'Form must have 4 fields'
        form = SubscriptionForm()
        fields = ['name',
                  'email',
                  'cpf',
                  'phone']
        self.assertItemsEqual(fields, form.fields)

    def test_cpf_is_digit(self):
        form = self.make_validated_form(cpf='ABCDE123456')
        form.is_valid()

        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf='123456')
        form.is_valid()

        self.assertItemsEqual(['cpf'], form.errors)

    def test_email_is_optional(self):
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(name='Elton Pereira de Lima',
                    email='eltonplima@gmail.com',
                    cpf='12345678901',
                    phone='82-96317900')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
