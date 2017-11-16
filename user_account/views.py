from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from .forms import CustomUserCreationForm

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
        return HttpResponseRedirect('/network')
    else:
        return HttpResponseRedirect('/')

def subscribe_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/about')
    else:
        form = CustomUserCreationForm()
        args = {'form': form}
        return render(request, 'accounts/subscribe.html', args)
