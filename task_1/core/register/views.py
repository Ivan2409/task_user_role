from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login as auth_login

from core.register.forms import RegisterForm
from app.models import UserModel, CustomUserRole


@csrf_protect
def register(request):
    template = 'admin/register/register.html'
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            paswd = register_form.cleaned_data['password']
            passwd_rep = register_form.cleaned_data['repeat_password']
            email = register_form.cleaned_data['email']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']

            if paswd != passwd_rep:
                error_messages = 'Please correct passwords.'
                data = {'form': register_form, 'error_messages': error_messages}
                return render(request, template, data)

            if UserModel.objects.filter(email=email).exists():
                error_messages = 'User with email: {} already exists.'.format(email)
                data = {'form': register_form, 'error_messages': error_messages}
                return render(request, template, data)

            user_role = CustomUserRole.objects.get(id=3)
            create_user = UserModel.objects.create_user(email=email, password=paswd, first_name=first_name,
                                                        last_name=last_name, role=user_role)
            # Auth user
            auth_login(request, create_user)
            return HttpResponseRedirect('/dashboard/')


        else:
            error_messages = 'Please correct fields.'
            data = {'form': register_form, 'error_messages': error_messages}
            return render(request, template, data)

    else:
        register_form = RegisterForm()

    return render(request, template, {'form': register_form})
