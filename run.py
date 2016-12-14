import sys
from populus import Project
import time


def transfer_callback(log_entry):

    print "Email created for: {}".format(log_entry['args']['sender'])


def main(argv):

    action = argv[0]
    address = None
    email = None

    if action == 'register':
        address = argv[1]
        email = argv[2]
    elif action == 'verify':
        address = argv[1]
        email = argv[2]
    elif action == 'owner':
        email = argv[1]
    elif action == 'remove':
        email = argv[1]
    else:
        print 'invalid action'
        exit(2)

    project = Project()
    with project.get_chain('local_test') as chain:
        print('\n\ncoinbase: {}'.format(chain.web3.eth.coinbase))

        # Call contract
        time.sleep(1)   # Otherwise locked??
        contract = chain.get_contract('IdentityRegistry9')

        #registered_event = contract.on("EmailAddressRegistered", {})
        #registered_event.watch(transfer_callback)
        #print 'contract owner: {}'.format(contract.call().owner())

        # Add in registry
        if action == 'register':

            set_txn_hash = contract.transact().registerEmailAddress(address, email)
            chain.wait.for_receipt(set_txn_hash)
            print 'added: {} for {}'.format(email, address)

        elif action == 'verify':
            verify = contract.call().verifyEmailAddress(address, email)
            print 'verified: {} for {} = {}'.format(email, address, verify)

        elif action == 'owner':
            owner = contract.call().getEmailAddressOwner(email)
            print 'owner: {}'.format(owner)

        elif action == 'remove':
            # remove from registry
            set_txn_hash = contract.transact().removeEmailAddress(email)
            chain.wait.for_receipt(set_txn_hash)
            print 'removed: {}'.format(email)

if __name__ == "__main__":
    main(sys.argv[1:])