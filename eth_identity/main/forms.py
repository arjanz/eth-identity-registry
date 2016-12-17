from django import forms


class RegistryEmailForm(forms.Form):
    ethereum_address = forms.CharField(max_length=64)
    email_address = forms.EmailField()
