"""eth_identity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from main.views import verify_email, verify_email_sent, verify_email_hash

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', verify_email, name='verify_email'),
    url(r'^sent/$', verify_email_sent, name='verify_email_sent'),
    url(r'^verify/(?P<email_id>[\w]+)/(?P<hash>[\w]+)/$', verify_email_hash, name='verify_email_hash'),
]
