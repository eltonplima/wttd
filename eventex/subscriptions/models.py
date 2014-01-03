# coding: utf-8

from django.db import models
from django.utils.translation import ugettext as _

class Subscription(models.Model):
    name = models.CharField(_(u'nome'), max_length=100)
    cpf = models.CharField(_(u'CPF'), max_length=11, unique=True)
    email = models.EmailField(_(u'email'), unique=True, blank=True)
    phone = models.CharField(_(u'telefone'), max_length=20, blank=True)
    created_at = models.DateTimeField(_(u'criado em'), auto_now_add=True)
    paid = models.BooleanField(_('Pago'), default=False)

    class Meta:
        ordering = ['created_at']
        verbose_name = _(u'inscrição')
        verbose_name_plural = _(u'inscrições')

    def __unicode__(self):
        return self.name
