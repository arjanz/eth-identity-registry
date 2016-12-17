import os
import sys

import time
from django.conf import settings
from django.core.management import BaseCommand
from populus import Project

from main.indentity_registry import IdentityRegistry


class Command(BaseCommand):
    help = "Verify e-mail in registry"

    def add_arguments(self, parser):
        # Named (optional) arguments
        #parser.add_argument('--license', help='Set License to generate stock')
        parser.add_argument('email', nargs='+', type=str)
        parser.add_argument('eth_address', nargs='+', type=str)
        pass

    def handle(self, *args, **options):
        registry = IdentityRegistry()
        registry.register_email(email=options['email'][0], eth_address=options['eth_address'][0])
