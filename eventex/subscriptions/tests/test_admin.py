# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionAdmin
from eventex.subscriptions.admin import Subscription
from eventex.subscriptions.admin import admin
from mock import Mock


class MakeAsPaidTest(TestCase):
    def setUp(self):
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)
        Subscription.objects.create(name='Elton Pereira de Lima',
                                    cpf='22233344455',
                                    email='foo@bar.com')

    def test_has_action(self):
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())