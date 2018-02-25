from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from core.login.forms import LoginForm
from app.models import UserModel

@csrf_protect
def login(request):
    template = 'admin/login/login.html'
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            if UserModel.objects.filter(email=email).exists():
                user = authenticate(username=email, password=password)
                if user:
                    if user.is_active:

                        auth_login(request, user)
                        return HttpResponseRedirect('/dashboard/')

                    else:
                        error_messages = 'User deactivated!'
                        data = {'form': login_form, 'error_messages': error_messages}
                        return render(request, template, data)
                else:
                    error_messages = 'Email or password wrong.'
                    data = {'form': login_form, 'error_messages': error_messages}
                    return render(request, template, data)
            else:
                error_messages = 'Email or password wrong.'
                data = {'form': login_form, 'error_messages': error_messages}
                return render(request, template, data)
    else:
        login_form = LoginForm()

    return render(request, template, {'form': login_form})


@login_required
def logout(request):
    django_logout(request)
    return redirect('/login/')