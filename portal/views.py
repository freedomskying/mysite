from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from portal.forms import LoginForm
import logging.handlers

logger = logging.getLogger('')


def portal(request):
    return render(request, 'portal/login.html')


def welcome(request):
    return render(request, 'portal/welcome.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = ''
        if form.is_valid():
            username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('portal:welcome'))

        else:
            # 登陆失败
            return render(request, 'portal/login.html', {'form': form,
                                                         'message': 'Wrong password. Please try again.'})
    else:
        form = LoginForm()

    return render(request, 'portal/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return render(request, 'portal/login.html')
