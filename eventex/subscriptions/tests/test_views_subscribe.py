from django.core.urlresolvers import reverse
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        'GET /inscricao/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_form.html')

    def test_html(self):
        'HTML must have contains input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the subscription form'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Elton Pereira',
                    cpf='12345678901',
                    email='eltonplima@gmail.com',
                    phone='82-96317900')
        self.resp = self.client.post(reverse('subscribe'), data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Elton Pereira',
                    cpf='000000000066',
                    email='eltonplima@gmail.com',
                    phone='82-96317900')
        self.resp = self.client.post(reverse('subscribe'), data)

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        self.assertFalse(Subscription.objects.exists())
