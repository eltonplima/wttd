# coding: utf-8
from django.core.urlresolvers import reverse
from django.test.testcases import TestCase
from eventex.subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        data = dict(name='Elton Pereira',
                    cpf='000000000066',
                    email='eltonplima@gmail.com',
                    phone='82-96317900')
        s = Subscription.objects.create(**data)

        url = reverse('subscription:detail', args=(s.id,))

        self.resp = self.client.get(url)

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_reverse(self):
        url = reverse('subscription:detail', args=(1,))
        self.assertEqual('/inscricao/1/', url)

    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        self.assertContains(self.resp, 'Elton Pereira')


class DetailNotFound(TestCase):
    def test_not_found(self):
        url = reverse('subscription:detail', args=(0,))
        resp = self.client.get(url)
        self.assertEqual(404, resp.status_code)