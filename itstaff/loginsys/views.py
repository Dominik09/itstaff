from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from loginsys.forms import RegistrationForm
from .models import User, Portfolio
import datetime

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')

def registration(request):
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    if request.POST:
        newuser_form = RegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username = newuser_form.cleaned_data['username'], password = newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)

def main_page(request):
    return render_to_response('main.html', {'username': auth.get_user(request).username})

def get_profile(request, Uid):
    args = {}
    args['user'] = User.objects.get(id = Uid)
    args['age'] = 20
    args['portfolio'] = Portfolio.objects.filter(user_id = Uid)

    return render_to_response('profile.html', args)

def edit_profile(request, Uid):
    """
    Редактирование профиля
    """
    pass