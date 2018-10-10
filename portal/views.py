from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from portal.forms import LoginForm, RegistrationForm
from portal.models import UserProfile


def portal(request):
    return render(request, 'portal/login.html')


def test(request):
    return render(request, 'portal/test.html')


def welcome(request):
    return render(request, 'portal/welcome.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
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


def register(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            # 使用内置User自带create_user方法创建用户，不需要使用save()
            user = User.objects.create_user(username=username, password=password, email=email)

            # 如果直接使用objects.create()方法后不需要使用save()
            user_profile = UserProfile(user=user)
            user_profile.save()

            return HttpResponseRedirect("/accounts/login/")
    else:
        form = RegistrationForm()
    return render(request, 'portal/registration.html', {'form': form})


def profile(request):
    return render(request, 'users/registration.html')


def profile_update(request):
    return 1


def pwd_change(request):
    return 1


def logout(request):
    auth.logout(request)
    return render(request, 'portal/login.html')
