# coding: utf-8
from datetime import datetime
from django.db import IntegrityError
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(name='Elton Pereira',
                                cpf='12345678901',
                                email='eltonplima@gmail.com',
                                phone='82-96317900')

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Elton Pereira', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='Elton Pereira',
                                    cpf='12345678901',
                                    email='eltonplima@gmail.com',
                                    phone='82-96317900')

    def test_cpf(self):
        s = Subscription(name='Elton Pereira',
                         cpf='12345678901',
                         email='eltonplima@gmail.com',
                         phone='82-96317900')
        self.assertRaises(IntegrityError, s.save)

    def test_email(self):
        s = Subscription(name='Elton Pereira',
                         cpf='12345678900',
                         email='eltonplima@gmail.com',
                         phone='82-96317900')
        self.assertRaises(IntegrityError, s.save)
