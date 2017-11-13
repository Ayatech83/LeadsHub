from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from custom_user.forms import CustomUserCreationForm

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'user_account/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else
        return HttpResponseRedirect('/accounts/invalid')
