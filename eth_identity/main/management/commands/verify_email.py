import os
import sys

import time
from django.conf import settings
from django.core.management import BaseCommand
from populus import Project

class Command(BaseCommand):
    help = "Generate stock"

    def add_arguments(self, parser):
        # Named (optional) arguments
        #parser.add_argument('--license', help='Set License to generate stock')
        pass

    def handle(self, *args, **options):
        sys.stdout.write('init project')
        os.chdir('/Users/arjan/Development/eth-identity-registry')
        project = Project()
        with project.get_chain('local_test') as chain:
            print('\n\ncoinbase: {}'.format(chain.web3.eth.coinbase))

            # Call contract
            time.sleep(1)  # Otherwise locked??
            contract = chain.get_contract('IdentityRegistry9')

            print 'contract owner: {}'.format(contract.call().owner())

            # Add in registry
            set_txn_hash = contract.transact().registerEmailAddress('0x6ac449bb22d99493e7a220d2a93d5de8e60c5c03',
                                                                    'test@test.com')
            chain.wait.for_receipt(set_txn_hash)

            verify = contract.call().verifyEmailAddress('0x6ac449bb22d99493e7a220d2a93d5de8e60c5c03', 'test@test.com')
            print 'verify: {}'.format(verify)

            owner = contract.call().getEmailAddressOwner('test@test.com')
            print 'owner: {}'.format(owner)



