# coding: utf-8
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.context_processors import csrf
from django.contrib import auth
from .models import User
from django.contrib.auth.forms import UserCreationForm
from loginsys.forms import RegistrationForm

def login(request):
    if str(request.user) is not 'AnonymousUser':
        return redirect('/')
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

def register(request):
    args = {}
    args.update(csrf(request))
    if str(request.user) is not 'AnonymousUser':
        args['user'] = User.objects.get(username = request.user)
    args['form'] = RegistrationForm()
    if request.POST:
        newuser_form = RegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(
                username = newuser_form.cleaned_data['username'],
                password = newuser_form.cleaned_data['password2']
            )
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)

def main_page(request):
    args = {}
    if str(request.user) is not 'AnonymousUser':
        args['user'] = User.objects.get(username = request.user)
    return render_to_response('main.html', args)

def my_profile(request, Uid):
    args = {}
    if str(request.user) is not 'AnonymousUser':
        args['user'] = User.objects.get(username = request.user)

    return render_to_response('profile.html', args)

def test(request):
    args={}
    args['user'] = request.user
    return render_to_response('test.html', args)