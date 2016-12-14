from django.shortcuts import render


def verify_email(request):
    
    return render(request, 'main/verify_email.html', context)