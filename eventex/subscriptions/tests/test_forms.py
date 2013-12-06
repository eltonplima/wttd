from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeFormTest(TestCase):
    def test_has_fields(self):
        'Form must have 4 fields'
        form = SubscriptionForm()
        fields = ['name',
                  'email',
                  'cpf',
                  'phone']
        self.assertItemsEqual(fields, form.fields)
