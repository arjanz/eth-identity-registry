from __future__ import unicode_literals

from django.db import models


class Account(models.Model):
    eth_address = models.CharField(max_length=64, verbose_name=u"Ethereum address", db_index=True)
    created = models.DateTimeField(auto_now_add=True)


class Emailaddress(models.Model):
    account = models.ForeignKey(Account)
    email = models.EmailField(db_index=True)
    verification_code = models.CharField(max_length=8)
    verified = models.BooleanField(default=False)

    class Meta:
        unique_together = (('account', 'email'),)

