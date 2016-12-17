import time

from populus import Project


class IdentityRegistry(object):

    def run_action(self, action, email=None, eth_address=None):
        project = Project()
        with project.get_chain('local') as chain:

            # Call contract
            time.sleep(1)  # Otherwise locked??
            contract = chain.get_contract('IdentityRegistry')

            # registered_event = contract.on("EmailAddressRegistered", {})
            # registered_event.watch(transfer_callback)
            # print 'contract owner: {}'.format(contract.call().owner())

            # Add in registry
            if action == 'register':
                print 'Adding: {} for {}...'.format(email, eth_address)
                set_txn_hash = contract.transact().registerEmailAddress(eth_address, email)
                print 'waiting for confirmation...'
                chain.wait.for_receipt(set_txn_hash)
                print 'added: {} for {}'.format(email, eth_address)

            elif action == 'verify':
                verify = contract.call().verifyEmailAddress(eth_address, email)
                print 'verified: {} for {} = {}'.format(email, eth_address, verify)
                return verify

            elif action == 'owner':
                owner = contract.call().getEmailAddressOwner(email)
                print 'owner: {}'.format(owner)
                return owner

            elif action == 'remove':
                # remove from registry
                print 'Removing: {}...'.format(email)
                set_txn_hash = contract.transact().removeEmailAddress(email)
                print 'waiting for confirmation...'
                chain.wait.for_receipt(set_txn_hash)
                print 'removed: {}'.format(email)

    def register_email(self, email, eth_address):
        return self.run_action(action='register', email=email, eth_address=eth_address)

    def verify_email(self, email, eth_address):
        return self.run_action(action='verify', email=email, eth_address=eth_address)

    def get_owner(self, email):
        return self.run_action(action='owner', email=email)

    def remove_email(self, email):
        return self.run_action(action='remove', email=email)
