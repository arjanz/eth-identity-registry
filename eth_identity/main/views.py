import uuid

from django.core.mail import send_mail
from django.core.management import call_command
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from populus import Project

from main.forms import RegistryEmailForm
from main.indentity_registry import IdentityRegistry
from main.models import Account, Emailaddress


def verify_email(request):

    if request.method == 'POST':

        form = RegistryEmailForm(request.POST)

        if form.is_valid():
            account, created = Account.objects.get_or_create(eth_address=form.cleaned_data['ethereum_address'])
            emailAddress, created = Emailaddress.objects.get_or_create(
                account=account,
                email=form.cleaned_data['email_address'],
            )

            emailAddress.verification_code = uuid.uuid4().hex

            emailAddress.save()

            send_mail(
                'Verify your e-mail address',
                'Click on following link to verify that this e-mail address is owned by Ethereum account {addr}:\n\n'
                'http://{host}/verify/{email_id}/{hash}/'.format(
                    addr=account.eth_address,
                    host=request.META['HTTP_HOST'],
                    email_id=emailAddress.id,
                    hash=emailAddress.verification_code
                ),
                'Eth Identity Registry <test@test.com>',
                [emailAddress.email],
                fail_silently=False,
            )

            # Sent e-mail
            return HttpResponseRedirect(reverse('verify_email_sent'))
    else:
        form = RegistryEmailForm()

    return render(request, 'main/verify_email.html', {'form': form})


def verify_email_sent(request):
    return render(request, 'main/verify_email_sent.html', {})


def verify_email_hash(request, email_id, hash):

    try:
        email_address = Emailaddress.objects.get(id=email_id, verification_code=hash, verified=False)

        registry = IdentityRegistry()

        # Register email in registry
        registry.register_email(email=email_address.email, eth_address=email_address.account.eth_address)

        # Verify email
        verified = registry.verify_email(email=email_address.email, eth_address=email_address.account.eth_address)

        if verified:
            # Update link
            email_address.verified = True
            email_address.save()

    except Emailaddress.DoesNotExist:
        raise Http404

    return render(request, 'main/verify_email_hash.html', {
        'email': email_address.email,
        'eth_address': email_address.account.eth_address,
        'verified': verified,
    })
